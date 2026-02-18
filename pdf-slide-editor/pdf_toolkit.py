"""
PDF Slide Editor Toolkit — PDFスライド修正用の再利用可能な関数群

使い方:
  from pdf_toolkit import (
      page_to_image, estimate_bg_color, remove_logo_pixels,
      fill_with_smooth_bg, fix_bottom_white, remove_text_by_coords,
      detect_white_boundary, assemble_pdf
  )

依存: pip3 install PyMuPDF Pillow numpy scipy
"""

import fitz
import numpy as np
from PIL import Image
from scipy.ndimage import uniform_filter1d


def page_to_image(doc, page_idx: int, dpi: int = 200) -> Image.Image:
    """PyMuPDFのページをPillow画像に変換"""
    page = doc[page_idx]
    pix = page.get_pixmap(dpi=dpi)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def estimate_bg_color(arr: np.ndarray) -> np.ndarray:
    """ページ上端中央から背景色を推定（ロゴやコンテンツが少ない領域）"""
    h, w = arr.shape[:2]
    return np.median(
        arr[3:25, w // 3 : w * 2 // 3, :].reshape(-1, 3), axis=0
    )


def remove_logo_pixels(arr: np.ndarray, logo_y1=None, logo_y2=None,
                        logo_x1=None, logo_x2=None) -> np.ndarray:
    """右下のロゴをピクセル単位で除去。
    座標省略時はデフォルト位置（右下70px×340px）を使用。"""
    h, w = arr.shape[:2]
    if logo_y1 is None:
        logo_y1 = h - 70
    if logo_y2 is None:
        logo_y2 = h - 2
    if logo_x1 is None:
        logo_x1 = w - 340
    if logo_x2 is None:
        logo_x2 = w - 2

    if logo_y1 < 0 or logo_x1 < 0:
        return arr

    # ロゴ直上の行から列ごとの背景色を取得
    ref_rows = arr[max(logo_y1 - 12, 0):logo_y1, logo_x1:logo_x2, :].astype(np.float32)
    if ref_rows.size == 0:
        return arr

    col_bg = np.median(ref_rows, axis=0).astype(np.uint8)

    for y in range(logo_y1, min(logo_y2, h)):
        for x in range(logo_x1, min(logo_x2, w)):
            lx = x - logo_x1
            pixel_b = arr[y, x, :].mean()
            bg_b = col_bg[lx, :].mean()
            # 背景より暗いピクセル（ロゴ文字・アイコン）を背景色に置換
            if pixel_b < bg_b - 5:
                arr[y, x, :] = col_bg[lx, :]

    return arr


def fill_with_smooth_bg(arr: np.ndarray, cut_y: int) -> np.ndarray:
    """cut_y以下を境界付近の背景色でスムーズに埋める。
    列ごとに背景色をサンプリングし、微小ノイズで自然さを維持。"""
    h, w = arr.shape[:2]
    fill_height = h - cut_y
    if fill_height <= 0:
        return arr

    # 境界直上から列ごとの背景色を推定
    ref_start = max(cut_y - 25, 0)
    ref_end = max(cut_y - 2, ref_start + 1)
    ref_rows = arr[ref_start:ref_end, :, :].astype(np.float32)
    col_bg = np.percentile(ref_rows, 90, axis=0)

    # ページ全体の背景色（グラデーションのアンカー）
    global_bg = estimate_bg_color(arr)

    # 列方向の平滑化（隣接列との差を抑える）
    for ch in range(3):
        col_bg[:, ch] = uniform_filter1d(col_bg[:, ch], size=80)

    # 充填: 微小ランダムノイズで均一感を防ぐ
    rng = np.random.default_rng(42)
    for y in range(fill_height):
        t = min(y / max(fill_height - 1, 1), 1.0)
        # 下に行くほどグローバル背景色に寄せる
        row_bg = col_bg * (1 - t * 0.3) + global_bg * (t * 0.3)
        noise = rng.normal(0, 1.5, (w, 3))
        row = np.clip(row_bg + noise, 0, 255).astype(np.uint8)
        arr[cut_y + y, :, :] = row

    # 境界グラデーション（元画像と新背景をブレンド）
    blend_px = min(15, fill_height)
    for dy in range(blend_px):
        y = cut_y + dy
        if y >= h:
            break
        alpha = dy / blend_px
        y_above = max(cut_y - 1, 0)
        arr[y] = (arr[y].astype(np.float32) * alpha +
                  arr[y_above].astype(np.float32) * (1 - alpha)).astype(np.uint8)

    return arr


def fix_bottom_white(arr: np.ndarray) -> np.ndarray:
    """下部の純白ピクセルを背景色に置換（軽微な修正向け）"""
    h, w = arr.shape[:2]
    bg = estimate_bg_color(arr)

    scan_start = int(h * 0.70)
    for y in range(scan_start, h):
        for x in range(w):
            pixel = arr[y, x, :].astype(np.float32)
            min_ch = pixel.min()
            if min_ch > 248:
                arr[y, x, :] = bg.astype(np.uint8)
            elif min_ch > 238:
                alpha = (min_ch - 238) / 10.0
                arr[y, x, :] = (pixel * (1 - alpha) + bg * alpha).astype(np.uint8)

    return arr


def remove_text_by_coords(arr: np.ndarray, x1: int, y1: int,
                           x2: int, y2: int) -> np.ndarray:
    """指定座標範囲のテキスト（暗いピクセル）を背景色で塗りつぶす"""
    h, w = arr.shape[:2]
    x1 = max(x1, 0)
    y1 = max(y1, 0)
    x2 = min(x2, w)
    y2 = min(y2, h)

    # テキスト上方から背景色をサンプリング
    ref_y1 = max(y1 - 20, 0)
    ref_y2 = max(y1 - 2, ref_y1 + 1)
    ref_region = arr[ref_y1:ref_y2, x1:x2, :].astype(np.float32)
    if ref_region.size > 0:
        bg_color = np.median(ref_region.reshape(-1, 3), axis=0).astype(np.uint8)
    else:
        bg_color = estimate_bg_color(arr).astype(np.uint8)

    bg_brightness = float(bg_color.mean())

    for y in range(y1, y2):
        for x in range(x1, x2):
            pixel_brightness = arr[y, x, :].mean()
            # テキスト（暗い）ピクセルだけ置換、背景はそのまま
            if pixel_brightness < bg_brightness - 10:
                arr[y, x, :] = bg_color

    return arr


def detect_white_boundary(arr: np.ndarray, bg_color: np.ndarray) -> int:
    """背景色との相対比較で白領域の開始位置を検出。
    下端から上方向にスキャンし、コンテンツまたは背景テクスチャのある行を見つける。"""
    h, w = arr.shape[:2]
    bg_brightness = float(bg_color.mean())

    for y in range(h - 1, int(h * 0.60), -1):
        row = arr[y, 50:w-50, :]
        # コンテンツ（テキスト等の暗いピクセル）がある行
        dark_pixel_ratio = (row.mean(axis=1) < bg_brightness - 15).mean()
        if dark_pixel_ratio > 0.02:
            return y + 1
        # 背景テクスチャ（回路パターン等）がある行: 背景色に近い
        row_brightness = float(row.mean())
        if abs(row_brightness - bg_brightness) < 5:
            return y + 1

    return h


def assemble_pdf(pages: list, output_path: str, dpi: int = 200):
    """Pillow画像リストをPDFとして保存"""
    pages[0].save(
        output_path,
        save_all=True,
        append_images=pages[1:],
        resolution=dpi,
        quality=95,
    )


# --- 分析ユーティリティ ---

def analyze_page(doc, page_idx: int, dpi: int = 200):
    """1ページの基本情報を分析して表示"""
    img = page_to_image(doc, page_idx, dpi)
    arr = np.array(img)
    h, w = arr.shape[:2]
    bg = estimate_bg_color(arr)

    has_text_layer = bool(doc[page_idx].get_text().strip())

    print(f"P{page_idx+1}: {w}x{h} bg=RGB({bg[0]:.0f},{bg[1]:.0f},{bg[2]:.0f}) "
          f"text_layer={'YES' if has_text_layer else 'NO'}")

    # 下部の白領域チェック
    white_start = detect_white_boundary(arr, bg)
    if white_start < h - 10:
        white_pct = (h - white_start) / h * 100
        print(f"  → 白領域: y={white_start} ({white_start/h*100:.0f}%) "
              f"残り{white_pct:.0f}%が白")

    # 右下ロゴチェック
    logo_region = arr[h-70:h-2, w-340:w-2, :]
    logo_dark = (logo_region.mean(axis=2) < 150).mean()
    if logo_dark > 0.005:
        print(f"  → 右下ロゴ検出: dark_ratio={logo_dark:.3f}")

    return arr


def analyze_pdf(input_path: str, dpi: int = 200):
    """PDF全体を分析"""
    doc = fitz.open(input_path)
    print(f"File: {input_path} ({doc.page_count} pages)\n")
    for i in range(doc.page_count):
        analyze_page(doc, i, dpi)
    doc.close()
