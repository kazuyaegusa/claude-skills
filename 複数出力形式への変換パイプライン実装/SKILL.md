# 複数出力形式への変換パイプライン実装

> 取得したWeChat記事を HTML/MHTML/Markdown/PDF/DOCX/CSV の6形式に変換可能にする

- 出典: https://github.com/qiye45/wechatDownload
- 投稿者: qiye45
- カテゴリ: automation-pipeline

## なぜ使うのか

用途によって最適なフォーマットが異なる（アーカイブならMHTML、分析ならCSV、文書化ならPDF等）ため、単一形式ではなく複数形式対応が実用上必須

## いつ使うのか

ダウンロードしたコンテンツを後続処理（検索・分析・アーカイブ・AI学習データ化）で利用する場合

## やり方

1. WeChat APIから記事のHTML本体を取得
2. 画像・動画・音声のメディアURLを抽出し、実ファイルをダウンロード
3. HTML→他形式の変換：
   - MHTML: リソース埋め込み形式で保存
   - Markdown: HTML解析→Markdown構文変換
   - PDF: HTML→PDF変換ライブラリ使用
   - DOCX: HTML→Word変換ライブラリ使用
   - CSV: メタデータ（タイトル・閲覧数・いいね数・コメント数・日付）を表形式で出力
4. ファイル名に日付プレフィックス追加（オプション）
5. 公式アカウント名でフォルダ分類

### 入力

- WeChat記事のHTML
- メディアファイルのURL一覧

### 出力

- HTML/MHTML/MD/PDF/DOCX/CSVファイル
- ダウンロードしたメディアファイル（画像・動画・音声）

## 使うツール・ライブラリ

- HTML→Markdown変換ライブラリ
- HTML→PDF変換（おそらくwkhtmltopdf/Playwright PDF等）
- HTML→DOCX変換（python-docx/pypandoc等）

## 前提知識

- WeChatアカウント（デスクトップ版またはモバイル版）
- HTTP通信の基本知識（トークン・認証ヘッダーの概念）
- MCP/Skillの基本概念（AIエージェントから外部ツールを呼び出す仕組み）
- Python環境（MCP実装を自前でカスタマイズする場合）
