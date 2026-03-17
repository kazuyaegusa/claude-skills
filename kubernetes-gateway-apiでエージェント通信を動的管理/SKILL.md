# Kubernetes Gateway APIでエージェント通信を動的管理

> Kubernetes上のエージェントをGateway APIのHTTPRoute/TLSRoute等で宣言的にルーティングし、agentgatewayのコントローラーが自動的にポリシーを反映する

- 出典: https://github.com/agentgateway/agentgateway
- 投稿者: agentgateway
- カテゴリ: agent-orchestration

## なぜ使うのか

Kubernetes環境でエージェントをスケールさせる際、ルーティング・認証・テナント分離を手動設定すると運用負荷が高いため、KubernetesネイティブなCRDで管理する

## いつ使うのか

Kubernetes上でエージェントをマイクロサービスとしてデプロイし、宣言的なインフラ管理を行いたい場合

## やり方

1. Kubernetes上にagentgatewayをデプロイ（Helmチャート等）
2. Gateway API CRD（Gateway, HTTPRoute等）を定義し、エージェントのServiceを参照
3. agentgatewayのKubernetesコントローラーがCRDを監視し、xDS経由で動的にルーティング・ポリシーを更新
4. エージェントからの通信がGatewayを経由してMCPサーバーへルーティングされ、RBAC・テナント分離が自動適用
5. CRD変更時にダウンタイムなく設定が反映される（xDS動的更新）

### 入力

- Kubernetes Gateway API CRD（Gateway, HTTPRoute等）
- エージェント・MCPサーバーのKubernetes Service

### 出力

- 動的にルーティングされるAgent通信
- K8s標準のオブザーバビリティ（Prometheus/Grafana等と統合可能）

## 使うツール・ライブラリ

- agentgateway Kubernetesコントローラー
- Kubernetes Gateway API
- xDS（Envoy互換動的設定プロトコル）

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
