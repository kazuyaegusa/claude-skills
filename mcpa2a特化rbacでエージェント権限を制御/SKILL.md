# MCP/A2A特化RBACでエージェント権限を制御

> agentgatewayのRBACシステムを使い、どのエージェントがどのMCPリソース（ツール・プロンプト・サンプリング）にアクセスできるかを定義する

- 出典: https://github.com/agentgateway/agentgateway
- 投稿者: agentgateway
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントが任意のツールを呼び出せると、機密データ漏洩や意図しない外部API課金が発生するリスクがあるため、ゲートウェイレベルで認可を強制する

## いつ使うのか

複数エージェントが異なる権限レベルでツールにアクセスする必要がある場合

## やり方

1. agentgatewayの設定ファイルでRole/PolicyをMCPリソース単位で定義（例: `tools:*`, `prompts:read`等）
2. エージェントにRoleを割り当て（テナント・ユーザー単位）
3. エージェントがMCP通信時にagentgatewayで認証・認可チェックが実行される
4. 権限がない場合は403エラーを返し、ログに記録
5. 必要に応じてRoleをCRDまたは設定ファイルで動的に更新

### 入力

- RBAC設定（Role/Policy定義）
- エージェント識別子（API Key, mTLS証明書等）

### 出力

- 認可されたMCP通信のみが通過
- アクセス拒否のログ・監査証跡

## 使うツール・ライブラリ

- agentgateway RBAC機能
- 認証バックエンド（OAuth2, mTLS等）

## 前提知識

- MCP（Model Context Protocol）の基本概念（ツール・プロンプト・サンプリング）
- A2A（Agent2Agent）プロトコルの仕組み
- API Gatewayの役割（認証・ルーティング・ログ集約）
- Kubernetes Gateway API（K8s環境の場合）
- xDS（Envoy互換動的設定プロトコル）の概要
