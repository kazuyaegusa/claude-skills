# オープンエコシステムによる280+統合の集約

> npmjs.comを統合パッケージのリポジトリとして使い、コミュニティが作成した統合（60%がコミュニティ貢献）を集約・バージョン管理する

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

中央集権的なプラットフォームに依存せず、npmのエコシステムを活用することで透明性と拡張性を確保するため

## いつ使うのか

大量の外部サービス統合が必要な場合、コミュニティによる貢献を促進したい場合、統合のバージョン管理と配布を効率化したい場合

## やり方

1. 統合をnpmパッケージ（@activepiecesスコープ）として公開する
2. npmjs.comで検索・インストール可能にする
3. ソースコードをGitHubリポジトリで公開する
4. コントリビューションガイドを提供し、コミュニティによるpieces作成を促進する
5. MITライセンス（Community Edition）とCommercial License（Enterprise）を使い分ける

### 入力

- npmパッケージ化された統合pieces
- GitHubリポジトリ

### 出力

- npmjs.comで公開された@activepieces/piece-*パッケージ
- 280以上の統合ライブラリ

## 使うツール・ライブラリ

- npm
- GitHub
- TypeScript

## 前提知識

- TypeScriptの基本知識
- Model Context Protocol（MCP）の概念理解
- Claude DesktopやCursorなどMCP対応ツールの使用経験
- npmパッケージの作成・公開方法
- ワークフロー自動化の基本概念（トリガー、アクション、データ変換）
- Docker/コンテナ技術の基本（セルフホスト時）
