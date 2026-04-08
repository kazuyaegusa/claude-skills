# PDF ロゴ除去

指定されたPDFファイルからロゴ/ウォーターマークを全ページ一括で除去する。

## 入力

`$ARGUMENTS`

## 実行手順

1. まず Read ツールで `/Users/kazuyaegusa/.claude/skills/pdf-logo-remover/SKILL.md` を読み、ツールの仕様を把握する。
2. 依存パッケージ（PyMuPDF, Pillow, numpy）がインストール済みか確認し、なければインストールする。
3. ユーザーが指定したPDFファイルパスを確認する。引数がない場合はカレントディレクトリのPDFファイルを一覧表示し、対象を質問する。
4. まず `--dry-run` でロゴ検出結果を表示し、検出位置が正しいかユーザーに確認する。
5. 確認後、実際にロゴ除去を実行する:
   ```bash
   python3 /Users/kazuyaegusa/.claude/skills/pdf-logo-remover/remove_pdf_logo.py <入力PDF>
   ```
6. 出力PDFの数ページをサンプルで画像変換し、ロゴが正しく除去されたかを目視確認する。
7. 問題があればオプション（`--corner`, `--scan-size`, `--dpi`）を調整して再実行する。
8. 結果をユーザーに報告する。
