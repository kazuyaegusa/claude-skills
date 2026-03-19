# オープンエコシステムによるコミュニティ駆動の拡張

> 全てのpieceをオープンソース（MIT）として公開し、npmjs.comでバージョン管理することで、コミュニティからの貢献（60%）を促進し、統合の種類と品質を組織的に拡大する

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

自動化プラットフォームの価値は統合の数と質に比例するが、単一組織だけでは全てのサービスをカバーできない。オープンソース化とnpmエコシステム活用により、世界中の開発者が貢献できる仕組みを作ることで、統合ライブラリを加速度的に成長させられる

## いつ使うのか

自社でカバーしきれないサービスとの統合をコミュニティの力で拡充したい時、オープンソースエコシステムとして自動化プラットフォームを成長させたい時

## やり方

1. 全pieceのソースコードをGitHubリポジトリで公開（MIT/Commercial Licenseデュアルライセンス）
2. Contributor's Guideを提供し、piece開発方法を明確化
3. コントリビュートされたpieceを自動的にnpmjs.comに公開
4. バージョン管理により、pieceの進化と後方互換性を保証
5. コミュニティが開発したpieceも自動的にMCPサーバーとして利用可能になる

### 入力

- GitHubリポジトリ
- Contributor's Guide
- npmjs.comアカウント
- コミュニティ貢献者

### 出力

- 200+のオープンソース統合piece
- コミュニティ貢献による継続的な機能拡張
- npmパッケージとして管理された統合ライブラリ

## 使うツール・ライブラリ

- GitHub
- npm
- MIT License
- Commercial License（エンタープライズ機能用）

## 前提知識

- TypeScriptの基礎知識（型システム、非同期処理）
- npmパッケージ管理の理解
- REST API/Webhook等の統合パターンの知識
- Model Context Protocol (MCP)の基本概念（LLMがツールを呼び出す仕組み）
- ワークフロー自動化ツール（Zapier等）の利用経験があると理解が早い

## 根拠

> You can easily create your own integration using our TypeScript framework. For detailed instructions, please refer to our [Contributor's Guide](https://www.activepieces.com/docs/build-pieces/building-pieces/overview).
