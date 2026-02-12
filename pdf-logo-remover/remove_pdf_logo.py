#!/usr/bin/env python3
"""
PDF Logo Remover — PDFの全ページから指定位置のロゴ/ウォーターマークを除去する汎用ツール

使い方:
  python3 remove_pdf_logo.py input.pdf [--output output.pdf] [--corner bottom-right]
                                        [--scan-size 300x60] [--dpi 150] [--dry-run]

依存: pip3 install PyMuPDF Pillow numpy
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional, Tuple

import fitz  # PyMuPDF
import numpy as np
from PIL import Image, ImageDraw


# --- 定数 ---
DARK_THRESHOLD = 180  # これ未満のRGB値を「暗い」ピクセルとみなす
UI_ELEMENT_BLUE_DIFF = 20  # B-R差がこれ以上ならダークブルーUI要素とみなす


def parse_args():
    parser = argparse.ArgumentParser(
        description="PDFの全ページからロゴ/ウォーターマークを除去する"
    )
    parser.add_argument("input", help="入力PDFファイルパス")
    parser.add_argument("--output", "-o", help="出力PDFファイルパス（省略時: *_clean.pdf）")
    parser.add_argument(
        "--corner",
        choices=["bottom-right", "bottom-left", "top-right", "top-left"],
        default=None,
        help="ロゴの位置（省略時: 自動検出）",
    )
    parser.add_argument(
        "--scan-size",
        default="300x60",
        help="ロゴ走査領域のサイズ WxH ピクセル（デフォルト: 300x60）",
    )
    parser.add_argument("--dpi", type=int, default=150, help="処理解像度（デフォルト: 150）")
    parser.add_argument("--dry-run", action="store_true", help="検出結果だけ表示して実際の除去はしない")
    return parser.parse_args()


def extract_page_image(page: fitz.Page, dpi: int) -> Image.Image:
    """PyMuPDFのページをPillow画像に変換"""
    pix = page.get_pixmap(dpi=dpi)
    return Image.frombytes("RGB", [pix.width, pix.height], pix.samples)


def detect_logo_corner(images: List[Image.Image], scan_w: int, scan_h: int) -> str:
    """全ページで一貫して暗いピクセルが存在するコーナーを検出してロゴ位置を推定する"""
    corners = {
        "bottom-right": lambda w, h: (w - scan_w, h - scan_h, w, h),
        "bottom-left": lambda w, h: (0, h - scan_h, scan_w, h),
        "top-right": lambda w, h: (w - scan_w, 0, w, scan_h),
        "top-left": lambda w, h: (0, 0, scan_w, scan_h),
    }

    scores = {}
    for corner_name, get_rect in corners.items():
        total_dark = 0
        for img in images:
            w, h = img.size
            x1, y1, x2, y2 = get_rect(w, h)
            region = np.array(img.crop((x1, y1, x2, y2)))
            dark_mask = np.all(region < DARK_THRESHOLD, axis=2)
            total_dark += np.sum(dark_mask)
        scores[corner_name] = total_dark

    best = max(scores, key=scores.get)
    print(f"[検出] ロゴ位置スコア: {scores}")
    print(f"[検出] 推定ロゴ位置: {best}")
    return best


def find_logo_bounds(
    images: List[Image.Image], corner: str, scan_w: int, scan_h: int
) -> Tuple[int, int, int, int]:
    """ロゴの正確なバウンディングボックスを全ページの暗いピクセルの和集合から算出する"""
    w, h = images[0].size

    # コーナーに応じた走査領域
    region_rects = {
        "bottom-right": (w - scan_w, h - scan_h, w, h),
        "bottom-left": (0, h - scan_h, scan_w, h),
        "top-right": (w - scan_w, 0, w, scan_h),
        "top-left": (0, 0, scan_w, scan_h),
    }
    rx1, ry1, rx2, ry2 = region_rects[corner]

    # 全ページの暗いピクセルの和集合マスクを作成
    union_mask = np.zeros((ry2 - ry1, rx2 - rx1), dtype=bool)
    for img in images:
        region = np.array(img.crop((rx1, ry1, rx2, ry2)))
        dark = np.all(region < DARK_THRESHOLD, axis=2)
        union_mask |= dark

    # マスクからバウンディングボックスを算出
    ys, xs = np.where(union_mask)
    if len(xs) == 0:
        print("[警告] ロゴのピクセルが検出されませんでした")
        return (rx1, ry1, rx2, ry2)

    # 余白を追加（上下左右5px）
    margin = 5
    logo_x1 = max(rx1 + int(xs.min()) - margin, rx1)
    logo_y1 = max(ry1 + int(ys.min()) - margin, ry1)
    logo_x2 = min(rx1 + int(xs.max()) + margin, rx2)
    logo_y2 = min(ry1 + int(ys.max()) + margin, ry2)

    print(f"[検出] ロゴ領域: ({logo_x1}, {logo_y1}) - ({logo_x2}, {logo_y2})")
    print(f"[検出] ロゴサイズ: {logo_x2 - logo_x1} x {logo_y2 - logo_y1} px")
    return (logo_x1, logo_y1, logo_x2, logo_y2)


def sample_background_color(arr: np.ndarray, logo_rect: tuple, corner: str) -> np.ndarray:
    """ロゴ周辺の背景色をサンプリングして中央値を返す"""
    lx1, ly1, lx2, ly2 = logo_rect
    h, w = arr.shape[:2]
    samples = []

    # ロゴの外側からサンプリング（上下左右）
    offsets = []
    if corner.startswith("bottom"):
        # ロゴの上側をサンプリング
        for x in np.linspace(lx1, lx2, 5, dtype=int):
            for dy in [-3, -5, -8]:
                y = ly1 + dy
                if 0 <= y < h and 0 <= x < w:
                    offsets.append((y, x))
        # ロゴの下側をサンプリング
        for x in np.linspace(lx1, lx2, 5, dtype=int):
            for dy in [3, 5]:
                y = ly2 + dy
                if 0 <= y < h and 0 <= x < w:
                    offsets.append((y, x))
    else:
        # ロゴの下側をサンプリング
        for x in np.linspace(lx1, lx2, 5, dtype=int):
            for dy in [3, 5, 8]:
                y = ly2 + dy
                if 0 <= y < h and 0 <= x < w:
                    offsets.append((y, x))

    if corner.endswith("right"):
        # 右側のサンプリング
        for y in np.linspace(ly1, ly2, 3, dtype=int):
            for dx in [3, 5]:
                x = lx2 + dx
                if 0 <= y < h and 0 <= x < w:
                    offsets.append((y, x))
    else:
        # 左側のサンプリング
        for y in np.linspace(ly1, ly2, 3, dtype=int):
            for dx in [-3, -5]:
                x = lx1 + dx
                if 0 <= y < h and 0 <= x < w:
                    offsets.append((y, x))

    for y, x in offsets:
        pixel = arr[y, x, :3]
        # 明るいピクセルのみ（UI要素を除外）
        if np.all(pixel > 150):
            samples.append(pixel)

    if not samples:
        # フォールバック: ロゴ領域の角のピクセル
        samples = [arr[ly1, lx1, :3]]

    return np.median(np.array(samples), axis=0).astype(np.uint8)


def is_ui_element_pixel(r: int, g: int, b: int) -> bool:
    """ダークカラーのUI要素（バー、ボタン等）のピクセルか判定"""
    return (
        int(r) < 80
        and int(g) < 80
        and int(b) < 120
        and int(b) > int(r) + UI_ELEMENT_BLUE_DIFF
    )


def has_overlapping_ui(arr: np.ndarray, logo_rect: tuple) -> bool:
    """ロゴ領域にUI要素（ダークバー等）が重なっているか判定"""
    lx1, ly1, lx2, ly2 = logo_rect
    region = arr[ly1:ly2, lx1:lx2, :3]
    ui_count = 0
    total = region.shape[0] * region.shape[1]
    for y in range(0, region.shape[0], 2):
        for x in range(0, region.shape[1], 2):
            r, g, b = region[y, x]
            if is_ui_element_pixel(r, g, b):
                ui_count += 1
    return ui_count > total * 0.01  # 1%以上ならUI要素あり


def remove_logo_simple(img: Image.Image, logo_rect: tuple, bg_color: tuple) -> Image.Image:
    """単純な矩形塗りつぶしでロゴを除去"""
    draw = ImageDraw.Draw(img)
    draw.rectangle(logo_rect, fill=bg_color)
    return img


def remove_logo_with_ui_protection(
    arr: np.ndarray, logo_rect: tuple, bg_color: np.ndarray, corner: str
) -> np.ndarray:
    """UI要素を保護しながらロゴを除去（ピクセルレベル処理）

    各x座標でUI要素の境界を検出し、それより外側（背景側）のみ塗りつぶす
    """
    lx1, ly1, lx2, ly2 = logo_rect

    for x in range(lx1, min(lx2, arr.shape[1])):
        if corner.startswith("bottom"):
            # 上から走査してUI要素の下端を見つける
            ui_end = ly1
            for y in range(ly1, min(ly2, arr.shape[0])):
                r, g, b = int(arr[y, x, 0]), int(arr[y, x, 1]), int(arr[y, x, 2])
                if is_ui_element_pixel(r, g, b):
                    ui_end = y + 1
            # UI要素の下からロゴ領域の下端まで背景色で塗る
            arr[ui_end : min(ly2, arr.shape[0]), x] = bg_color
        else:
            # 下から走査してUI要素の上端を見つける
            ui_start = ly2
            for y in range(ly2 - 1, max(ly1 - 1, -1), -1):
                r, g, b = int(arr[y, x, 0]), int(arr[y, x, 1]), int(arr[y, x, 2])
                if is_ui_element_pixel(r, g, b):
                    ui_start = y
            # ロゴ領域の上端からUI要素の上端まで背景色で塗る
            arr[max(ly1, 0) : ui_start, x] = bg_color

    return arr


def process_pdf(
    input_path: str,
    output_path: str,
    corner: Optional[str],
    scan_w: int,
    scan_h: int,
    dpi: int,
    dry_run: bool,
):
    doc = fitz.open(input_path)
    print(f"[入力] {input_path} ({len(doc)}ページ)")

    # 全ページを画像に変換
    print("[処理] ページ画像を抽出中...")
    images = []
    for i in range(len(doc)):
        images.append(extract_page_image(doc[i], dpi))
    print(f"[処理] 画像サイズ: {images[0].size[0]} x {images[0].size[1]} px (DPI={dpi})")

    # ロゴ位置の検出
    if corner is None:
        corner = detect_logo_corner(images, scan_w, scan_h)
    else:
        print(f"[設定] ロゴ位置: {corner}")

    # ロゴの正確な境界を検出
    logo_rect = find_logo_bounds(images, corner, scan_w, scan_h)

    if dry_run:
        print("[ドライラン] 検出結果のみ表示。--dry-run を外すと実際に除去します。")
        doc.close()
        return

    # 各ページのロゴを除去
    print("[処理] ロゴ除去中...")
    modified_images = []
    for i, img in enumerate(images):
        arr = np.array(img)
        bg_color = sample_background_color(arr, logo_rect, corner)
        bg_tuple = tuple(int(v) for v in bg_color)

        if has_overlapping_ui(arr, logo_rect):
            arr = remove_logo_with_ui_protection(arr, logo_rect, bg_color, corner)
            img = Image.fromarray(arr)
            print(f"  ページ {i + 1}: UI保護モード (背景 RGB{bg_tuple})")
        else:
            img = remove_logo_simple(img, logo_rect, bg_tuple)
            print(f"  ページ {i + 1}: 標準モード (背景 RGB{bg_tuple})")

        modified_images.append(img)

    doc.close()

    # PDF保存
    modified_images[0].save(
        output_path,
        "PDF",
        save_all=True,
        append_images=modified_images[1:],
        resolution=dpi,
    )
    print(f"\n[完了] {output_path}")


def main():
    args = parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"[エラー] ファイルが見つかりません: {input_path}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        output_path = args.output
    else:
        output_path = str(input_path.with_stem(input_path.stem + "_clean"))

    scan_w, scan_h = (int(x) for x in args.scan_size.split("x"))

    process_pdf(
        str(input_path),
        output_path,
        args.corner,
        scan_w,
        scan_h,
        args.dpi,
        args.dry_run,
    )


if __name__ == "__main__":
    main()
