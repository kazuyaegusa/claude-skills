---
name: pdf-slide-editor
description: PDFスライドの修正指示（ロゴ除去・白領域修正・テキスト除去・背景色調整など）を受けて、分析→スクリプト生成→実行→検証のサイクルで的確に反映するスキル。
---

# PDF Slide Editor

ユーザーの修正指示をPDFスライドに的確に反映する。

## 起動条件

以下のいずれかに該当する場合にこのスキルを使用する:
- PDFファイルの修正を依頼された
- PDFのロゴ除去、テキスト除去、背景修正を依頼された
- `/fix-pdf` コマンドが実行された

## 依存パッケージ

```
pip3 install PyMuPDF Pillow numpy scipy
```

## ツールキット

`/Users/kazuyaegusa/.claude/skills/pdf-slide-editor/pdf_toolkit.py`

再利用可能な関数群を提供。毎回カスタムスクリプトを生成する際にインポートして使う。

## 処理フロー（4フェーズ・厳守）

### Phase 1: 分析（推測するな、測定しろ）

ユーザーの指示を受けたら、**まず PDFをコードで分析して数値を得る**。目視だけで判断しない。

#### 1-1. 基本情報の取得

```python
import fitz
import numpy as np
from PIL import Image

doc = fitz.open('input.pdf')
DPI = 200  # 標準解像度

for i in range(doc.page_count):
    page = doc[i]
    pix = page.get_pixmap(dpi=DPI)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    arr = np.array(img)
    h, w = arr.shape[:2]

    # 背景色（上端中央から推定）
    bg = np.median(arr[3:25, w//3:w*2//3, :].reshape(-1, 3), axis=0)
    print(f"P{i+1}: {w}x{h} bg=RGB({bg[0]:.0f},{bg[1]:.0f},{bg[2]:.0f})")
```

#### 1-2. テキストレイヤーの有無確認

```python
# テキスト検索が使えるか確認（画像ベースPDFでは空になる）
text = page.get_text()
if text.strip():
    print("テキストレイヤーあり → search_for() でテキスト座標取得可能")
else:
    print("テキストレイヤーなし → 座標は画像分析で特定する")
```

**重要**: NotebookLM等が生成するPDFは**画像ベース**でテキストレイヤーがない。`search_for()` は使えないので、必ず座標ベースで処理する。

#### 1-3. 問題箇所の座標特定

各修正指示に対して、**ピクセル座標を数値で確認する**。

**ロゴ位置の特定:**
```python
# 右下領域で暗いピクセルのある行を探す
for y in range(h-100, h, 5):
    right_region = arr[y, w-400:, :]
    dark_ratio = (right_region.mean(axis=1) < 150).mean()
    if dark_ratio > 0.01:
        print(f"y={y} ({y/h*100:.1f}%): dark_ratio={dark_ratio:.3f}")
```

**白領域の境界特定:**
```python
bg_brightness = float(bg.mean())
for y in range(h-1, int(h*0.60), -1):
    row = arr[y, 50:w-50, :]
    row_brightness = float(row.mean())
    dark_pixel_ratio = (row.mean(axis=1) < bg_brightness - 15).mean()
    # コンテンツ（暗いピクセル）がある行 or 背景テクスチャがある行
    if dark_pixel_ratio > 0.02 or abs(row_brightness - bg_brightness) < 5:
        print(f"P{i+1} 白領域開始: y={y+1} ({(y+1)/h*100:.1f}%)")
        break
```

**テキスト座標の特定（画像ベースPDF）:**
```python
# 対象領域で暗いピクセルのx範囲を特定
for y in range(start_y, end_y, 5):
    row_region = arr[y, start_x:, :]
    dark_pixels = np.where(row_region.mean(axis=1) < 150)[0]
    if len(dark_pixels) > 0:
        x_min = dark_pixels[0] + start_x
        x_max = dark_pixels[-1] + start_x
        print(f"y={y}: text x range = {x_min}-{x_max}")
```

### Phase 2: スクリプト生成

Phase 1の分析結果を使って、**そのPDF専用のカスタム修正スクリプト**を生成する。

#### 設計ルール

1. **toolkit をインポート**して使う（関数を毎回再定義しない）
2. **DPI = 200** を標準とする
3. **処理順序を厳守**: ロゴ除去 → テキスト除去 → 白領域修正
4. **ページごとの処理パラメータ**を明示的に指定する（全ページ一律にしない）
5. **座標は Phase 1 の実測値**を使う（推測しない）

#### スクリプトテンプレート

```python
from pdf_toolkit import (
    page_to_image, estimate_bg_color, remove_logo_pixels,
    fill_with_smooth_bg, fix_bottom_white, remove_text_by_coords,
    detect_white_boundary
)
import fitz
import numpy as np
from PIL import Image

DPI = 200
INPUT = "input.pdf"
OUTPUT = "input_clean.pdf"

doc = fitz.open(INPUT)

# === ページごとの修正設定 ===
fix_white_pages = {1, 7, 8, 10}  # 白領域修正対象

# テキスト除去: {ページ番号: [(x1, y1, x2, y2), ...]}
text_coords = {
    10: [(3080, 1760, 3720, 1845)],  # Phase1で実測した座標
}

pages = []
for i in range(doc.page_count):
    img = page_to_image(doc, i, DPI)
    arr = np.array(img)
    h, w = arr.shape[:2]
    page_num = i + 1

    # 1. ロゴ除去（全ページ）
    arr = remove_logo_pixels(arr)

    # 2. テキスト除去（指定ページのみ）
    if page_num in text_coords:
        for coords in text_coords[page_num]:
            arr = remove_text_by_coords(arr, *coords)

    # 3. 白領域修正（指定ページのみ）
    if page_num in fix_white_pages:
        bg_color = estimate_bg_color(arr)
        white_start = detect_white_boundary(arr, bg_color)
        if white_start < h - 10:
            arr = fill_with_smooth_bg(arr, white_start)
    else:
        arr = fix_bottom_white(arr)

    pages.append(Image.fromarray(arr))

doc.close()
pages[0].save(OUTPUT, save_all=True, append_images=pages[1:], resolution=DPI, quality=95)
```

### Phase 3: 実行

```bash
python3 fix_script.py
```

### Phase 4: 検証

出力PDFを `Read` ツールで読み込んで視覚確認する。問題があれば Phase 1 に戻る。

## 失敗パターン（過去の教訓・絶対に繰り返さない）

| 失敗 | 原因 | 正しいアプローチ |
|------|------|----------------|
| テキスト検索が空で除去できない | 画像ベースPDFにsearch_for()を使った | Phase 1-2 でテキストレイヤー有無を確認。なければ座標指定 |
| 白領域が検出されない | 絶対閾値(>240)で判定した | 背景色との相対比較で判定する |
| ロゴ跡が不自然 | 一律の背景色で塗りつぶした | 周辺ピクセルから列ごとに背景色をサンプリング |
| 座標がずれている | 推測で座標を指定した | Phase 1 でピクセル座標を実測する |
| 処理後に別の問題が発生 | 処理順序が不適切 | ロゴ→テキスト→白領域の順序を厳守 |
| 白領域修正で背景が不自然 | 単純な塗りつぶし | fill_with_smooth_bg で境界ブレンド＋微小ノイズ |

## 背景色判定の原則

- **ページ上端中央**から背景色を推定する（ロゴやコンテンツが少ない領域）
- **相対比較**を使う: 「白かどうか」ではなく「背景色より明るいかどうか」
- **列ごと**にサンプリングする（横方向のグラデーションに対応）
- **微小ノイズ**を加える（均一塗りの不自然さを防ぐ）
