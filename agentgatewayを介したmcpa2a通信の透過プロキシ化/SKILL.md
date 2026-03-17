# agentgatewayを介したMCP/A2A通信の透過プロキシ化

> AIエージェントとMCPサーバー（またはAgent）間の通信をagentgatewayに中継させ、認証・監視・ポリシー適用を透過的に挟む

- 出典: https://github.com/agentgateway/agentgateway
- 投稿者: agentgateway
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェント自体にセキュリティ・ログ・ガバナンス機能を実装すると各エージェントの保守コストが増大し、統一的なポリシー管理が困難になるため、ゲートウェイで一元管理する

## いつ使うのか

複数エージェントが共通のツールセットにアクセスし、認証・ログ・レート制限を統一したい場合

## やり方

1. agentgatewayをローカルまたはKubernetes上でデプロイ（`agentgateway.dev/docs/quickstart`参照）
2. エージェントの接続先をMCPサーバー直接でなくagentgatewayのエンドポイントに設定
3. agentgatewayの設定ファイル（またはKubernetes Gateway API CRD）でRBAC・テナント・ルーティングルールを定義
4. エージェントからの通信がagentgatewayを経由してMCPサーバーへ到達し、ログ・認可が自動適用される

### 入力

- エージェントのMCP/A2A通信エンドポイント
- RBACポリシー・テナント情報（YAML/CRD）
- ターゲットMCPサーバーのアドレス

### 出力

- 透過的に認証・ログが記録されたAgent通信
- 統一されたアクセスログ・監視ダッシュボード（UI含む）

## 使うツール・ライブラリ

- agentgateway（Rust製バイナリ）
- Kubernetes Gateway API（K8s環境の場合）
- xDS（動的設定更新用）

## 前提知識

- MCP（Model Context Protocol）の基本概念（ツール・プロンプト・サンプリング）
- A2A（Agent2Agent）プロトコルの仕組み
- API Gatewayの役割（認証・ルーティング・ログ集約）
- Kubernetes Gateway API（K8s環境の場合）
- xDS（Envoy互換動的設定プロトコル）の概要

## 根拠

> 「agentgateway is an open source data plane optimized for agentic AI connectivity within or across any agent framework or environment」（投稿本文）

> 「Security First: agentgateway includes a robust MCP/A2A focused RBAC system」（投稿本文）

> 「Legacy API Support: agentgateway can transform legacy APIs into MCP resources. Currently supports OpenAPI」（投稿本文）

> 「Kubernetes Native: agentgateway includes a built-in Kubernetes controller for dynamic provisioning and management via the Kubernetes Gateway API」（投稿本文）

> 「Dynamic: agentgateway supports dynamic configuration updates via xDS, without any downtime」（投稿本文）
