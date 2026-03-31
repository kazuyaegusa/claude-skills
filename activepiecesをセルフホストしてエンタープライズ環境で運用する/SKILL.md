# Activepiecesをセルフホストしてエンタープライズ環境で運用する

> Activepiecesをオンプレミスまたはプライベートクラウドにデプロイし、ネットワークギャップ環境でも安全にワークフロー自動化を実現する

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

SaaSのワークフロー自動化ツールは外部通信が必須で、セキュリティポリシーや規制要件を満たせない場合がある。Activepiecesはセルフホスト可能でMITライセンスのため、組織内に完全に閉じた形で運用できる

## いつ使うのか

セキュリティ要件が厳しい、データを外部に出せない、カスタマイズ要件が多い場合

## やり方

1. デプロイガイド（https://www.activepieces.com/docs/install/overview）を参照
2. Docker ComposeまたはKubernetesで環境を構築
3. 開発者がpieceを開発・登録し、ノーコードユーザーがビルダーUIで利用
4. ブランディングや権限制御などエンタープライズ機能を設定（Enterprise Editionではコマーシャルライセンス）
5. Human-in-the-loop機能（承認待ち、遅延実行）やフォーム/チャットインターフェースを活用

### 入力

- インフラ環境（Docker/Kubernetes対応サーバー）
- 組織のセキュリティポリシー

### 出力

- セルフホストされたActivepieces環境
- 組織専用のワークフロー自動化基盤

## 使うツール・ライブラリ

- Docker
- Kubernetes
- Activepieces (Community Edition: MIT / Enterprise Edition: Commercial License)

## 前提知識

- TypeScriptの基礎知識（piece開発の場合）
- Docker/Kubernetesの基本操作（セルフホストの場合）
- ワークフロー自動化の概念理解
- MCPプロトコルの基本理解（LLM統合の場合）
