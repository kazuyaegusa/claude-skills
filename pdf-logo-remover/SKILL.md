---
name: pdf-logo-remover
description: PDFの全ページからロゴやウォーターマークを自動検出・除去するスキル。NotebookLM等のツールが付与するブランディングロゴの一括除去に対応。
---

# PDF Logo Remover

PDFの全ページから不要なロゴ/ウォーターマークを検出し、背景に自然に馴染む形で除去する。

## ツールスクリプト

`/Users/kazuyaegusa/.claude/skills/pdf-logo-remover/remove_pdf_logo.py`

## 依存パッケージ

```
pip3 install PyMuPDF Pillow numpy
```

## 使い方

### 基本（自動検出モード）

```bash
python3 /Users/kazuyaegusa/.claude/skills/pdf-logo-remover/remove_pdf_logo.py input.pdf
```

出力: `input_clean.pdf`

### オプション

| オプション | 説明 | デフォルト |
|-----------|------|-----------|
| `--output`, `-o` | 出力ファイルパス | `*_clean.pdf` |
| `--corner` | ロゴ位置 (`bottom-right`, `bottom-left`, `top-right`, `top-left`) | 自動検出 |
| `--scan-size` | ロゴ走査領域 `WxH` px | `300x60` |
| `--dpi` | 処理解像度 | `150` |
| `--dry-run` | 検出結果のみ表示 | - |

### 例

```bash
# NotebookLM PDFのロゴ除去（右下自動検出）
python3 remove_pdf_logo.py lecture.pdf

# 左下のロゴを指定して除去
python3 remove_pdf_logo.py report.pdf --corner bottom-left

# 大きめのロゴに対応（走査領域拡大）
python3 remove_pdf_logo.py slides.pdf --scan-size 400x100

# 高解像度で処理
python3 remove_pdf_logo.py slides.pdf --dpi 300 -o slides_final.pdf
```

## 処理ロジック

1. **全ページ画像変換**: PyMuPDFで各ページをラスタ画像に変換
2. **ロゴ位置自動検出**: 4隅の暗いピクセル密度を全ページで比較し、最もロゴらしい隅を特定
3. **ロゴ境界算出**: 全ページの暗ピクセルの和集合からバウンディングボックスを算出
4. **背景色適応サンプリング**: ページごとにロゴ周辺の背景色を中央値で推定
5. **UI要素保護**: ロゴ領域にダークカラーのUI要素（キーメッセージ帯等）が重なる場合、ピクセルレベルでUI要素を保護しつつロゴのみ除去
6. **PDF再構成**: Pillowで修正済み画像をPDFに再結合

## 注意事項

- 元のPDFがベクターの場合でもラスタ画像として再エンコードされる
- DPIを上げると品質は上がるがファイルサイズと処理時間が増加する
- ロゴが背景と同系色（透かし等）の場合は検出精度が下がる可能性がある
