# セルフホスト環境でワークフロー自動化をセキュアに構築する

> Activepiecesをセルフホスト（network-gapped）環境にデプロイし、企業内のセキュリティ要件を満たしながらワークフロー自動化を実現する

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

Zapier等のクラウドサービスではデータがサードパーティに送信されるが、セルフホストならデータを自組織内に留められる。ブランディング・権限管理も完全カスタマイズ可能

## いつ使うのか

機密データを扱うワークフロー自動化が必要な場合。コンプライアンス要件でクラウドサービス利用が制限されている場合

## やり方

1. Activepieces公式デプロイドキュメント（https://www.activepieces.com/docs/install/overview）を参照
2. DockerまたはKubernetes環境でActivepiecesをデプロイ
3. 環境変数でブランディング・認証・ネットワーク設定をカスタマイズ
4. 開発者が必要なpieceを追加し、非技術者がノーコードビルダーで利用
5. ワークフローをバージョン管理し、承認フロー（Human in the Loop）を組み込む

### 入力

- Docker / Kubernetes環境
- ネットワーク・セキュリティ要件
- ブランディング・認証設定

### 出力

- セルフホストされたワークフロー自動化環境
- カスタマイズ可能なノーコードビルダー
- 監査可能なワークフロー実行ログ

## 使うツール・ライブラリ

- Activepieces
- Docker
- Kubernetes

## 前提知識

- TypeScriptの基本知識（piece開発時）
- Docker/Kubernetesの基本（セルフホスト時）
- MCP（Model Context Protocol）の概念理解
- npmパッケージ管理の基礎
- REST API / Webhook の基本知識

## 根拠

> When you contribute pieces to Activepieces they become automatically available as MCP servers that you can use with LLMs through Claude Desktop, Cursor or Windsurf!

> All pieces are open source and available on npmjs.com, **60% of the pieces are contributed by the community**.

> Pieces are npm packages in TypeScript, offering full customization with the best developer experience, including **hot reloading** for **local** piece development on your machine.

> As an **open ecosystem**, all integration source code is accessible in our repository. These integrations are versioned and [published](https://www.npmjs.com/search?q=%40activepieces) directly to npmjs.com upon contribution.
