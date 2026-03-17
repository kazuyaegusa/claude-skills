# OpenAPIをMCPリソースに変換してエージェントに公開

> 既存のREST APIのOpenAPI定義をagentgatewayに読み込ませ、エージェントがMCPプロトコル経由で呼び出せるようにする

- 出典: https://github.com/agentgateway/agentgateway
- 投稿者: agentgateway
- カテゴリ: agent-orchestration

## なぜ使うのか

レガシーシステムのAPIをエージェントに使わせるために各エージェントにREST呼び出しコードを書くと保守性が悪化し、統一的なアクセス制御ができないため、ゲートウェイ側で変換層を提供する

## いつ使うのか

既存のREST APIをAgent向けに公開したいが、各エージェントにHTTPクライアントを実装したくない場合

## やり方

1. agentgatewayの設定で「Legacy API Support」機能を有効化
2. OpenAPI定義（YAML/JSON）をagentgatewayに登録（詳細はドキュメント参照）
3. agentgatewayが自動的にOpenAPIエンドポイントをMCPリソースとしてマッピング
4. エージェントはMCPクライアントとしてagentgateway経由でREST APIを呼び出す
5. agentgateway側でRBAC・ログ・レート制限を適用

### 入力

- OpenAPI 3.x定義ファイル
- バックエンドREST APIのベースURL

### 出力

- MCPプロトコルでアクセス可能なリソースエンドポイント
- 統一されたアクセスログ

## 使うツール・ライブラリ

- agentgateway（OpenAPIトランスフォーマー内蔵）
- OpenAPI 3.x定義

## 前提知識

- MCP（Model Context Protocol）の基本概念（ツール・プロンプト・サンプリング）
- A2A（Agent2Agent）プロトコルの仕組み
- API Gatewayの役割（認証・ルーティング・ログ集約）
- Kubernetes Gateway API（K8s環境の場合）
- xDS（Envoy互換動的設定プロトコル）の概要

## 根拠

> 「Legacy API Support: agentgateway can transform legacy APIs into MCP resources. Currently supports OpenAPI」（投稿本文）

> 「Kubernetes Native: agentgateway includes a built-in Kubernetes controller for dynamic provisioning and management via the Kubernetes Gateway API」（投稿本文）
