# 公式・評価済みServer優先

> 🎖️（公式実装）やGlamaスコアバッジで品質を判断し、信頼性の高いServerを選ぶ

- 出典: https://github.com/punkpeye/awesome-mcp-servers
- 投稿者: punkpeye
- カテゴリ: other

## なぜ使うのか

個人プロジェクトの中にはメンテナンスされていないものや不完全な実装が含まれるため、公式実装や評価済みのものを優先することでリスクを減らせる

## いつ使うのか

本番環境や重要なプロジェクトでMCP Serverを選定する時

## やり方

1. Server名の横に🎖️があれば公式実装として優先
2. Glamaバッジをクリックして評価ページを確認
3. GitHub Starsやコミット頻度も参考にする
4. 複数候補がある場合は公式 > 評価高 > 最新更新の順で選定

### 入力

- Server候補の品質指標（公式マーク、評価スコア、GitHub活動）

### 出力

- 信頼性の高いMCP Serverの選択結果

## 使うツール・ライブラリ

- Glama評価システム
- GitHub Stats

## 前提知識

- Model Context Protocol (MCP)の基本概念（Server/Client/Tools/Resources）
- Claude DesktopまたはMCP対応クライアントの使用経験
- GitHubの基本操作（リポジトリのクローン、README閲覧）
- JSON設定ファイルの編集方法
