# カテゴリ別Server検索

> 機能ドメイン（ファイルシステム、データベース、コミュニケーション等）ごとに分類されたMCP Serverリストから目的のServerを探す

- 出典: https://github.com/punkpeye/awesome-mcp-servers
- 投稿者: punkpeye
- カテゴリ: automation-pipeline

## なぜ使うのか

3000以上の実装を順番に確認するのは非効率であり、カテゴリ分類により必要な機能を持つServerを素早く特定できる

## いつ使うのか

特定のドメイン（例: メール送信、データベース操作）のMCP Serverを探す時

## やり方

1. README内の目次から該当カテゴリ（例: Databases, Communication）を選択
2. カテゴリ内のServer一覧を確認
3. 各Serverの説明・言語アイコン・対応プラットフォームを比較
4. GitHubリンクから実装詳細を確認

### 入力

- 実現したい機能のドメイン（例: Browser Automation, Finance）

### 出力

- 候補となるMCP ServerのGitHubリポジトリリスト

## 使うツール・ライブラリ

- GitHub検索
- Glamaバッジ

## 前提知識

- Model Context Protocol (MCP)の基本概念（Server/Client/Tools/Resources）
- Claude DesktopまたはMCP対応クライアントの使用経験
- GitHubの基本操作（リポジトリのクローン、README閲覧）
- JSON設定ファイルの編集方法
