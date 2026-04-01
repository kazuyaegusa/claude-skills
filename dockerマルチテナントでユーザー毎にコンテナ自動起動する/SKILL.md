# Dockerマルチテナントでユーザー毎にコンテナ自動起動する

> ユーザーごとに独立したDockerコンテナをオンデマンドで起動し、ルーターが自動振り分けを行うマルチテナント構成

- 出典: https://x.com/qingq77/status/2035241244289638417
- 投稿者: Geek Lite
- カテゴリ: agent-orchestration

## なぜ使うのか

複数ユーザーが同じエージェントを使う際、セッション・メモリ・ツールの分離が必要。Dockerで隔離すればリソース制限とセキュリティ境界を確保できる

## いつ使うのか

複数ユーザーにエージェントサービスを提供し、セッション・メモリ・リソースを完全分離したい時

### 具体的な適用場面

- 既存フレームワークの抽象化に不満があり、エージェントの挙動を完全制御したい
- 依存関係を最小化した本番運用可能なAIエージェントを構築したい
- Tool Use・記憶・自己修復の実装を学びたい
- DockerでマルチテナントAIエージェントを提供したい

## やり方

1. `router.py`がメッセージを受信 2. ユーザーIDからコンテナ名を決定 3. コンテナが存在しなければ`docker run`で自動起動 4. ヘルスチェックでコンテナ状態を確認 5. メッセージをコンテナ内エージェントに転送 6. 非アクティブなコンテナは自動停止

### 入力

- ユーザーID
- Dockerイメージ
- ルーター設定（ポート・ヘルスチェック）

### 出力

- ユーザー毎の独立コンテナ
- 自動起動・停止機構
- ヘルスチェック付きルーティング

## 使うツール・ライブラリ

- Docker
- docker-py（Dockerクライアント）

## 前提知識

- Python標準ライブラリの理解
- OpenAI Function Calling仕様の理解
- Docker基礎知識
- JSON-RPC基礎
- ベクトルDB（LanceDB）の基本
- ffmpegコマンドの基本

## 根拠

> 作者用 3500 行纯 Python、零框架依赖、8 个文件实现了完整的 Agent系统

> Tool Use Loop + 三层记忆体系（会话 → LLM 压缩长期记忆 → LanceDB向量检索）+ MCP 插件 + 定时任务 +自愈机制

> No LangChain, no LlamaIndex, no CrewAI -- just the standard library + 3 small packages (croniter, lancedb, websocket-client)

> Runtime Tool Creation -- The agent can write, save, and load new Python tools at runtime (create_tool)

> Self-Repair -- Daily self-check, session health diagnostics, error log analysis, auto-notification on failure
