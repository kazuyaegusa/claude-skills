# MCP JSON-RPCでstdio/HTTP経由でツールを動的追加する

> MCP（Model Context Protocol）サーバーをJSON-RPC経由で接続し、外部ツールを再起動なしで追加・更新する

- 出典: https://x.com/qingq77/status/2035241244289638417
- 投稿者: Geek Lite
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェント本体を再起動せずにツールを追加・更新したい。MCPを使えばstdio/HTTPでプラグインとして接続できる

## いつ使うのか

エージェントのツールセットを動的に拡張したい、外部システムとの連携をプラグイン化したい時

### 具体的な適用場面

- 既存フレームワークの抽象化に不満があり、エージェントの挙動を完全制御したい
- 依存関係を最小化した本番運用可能なAIエージェントを構築したい
- Tool Use・記憶・自己修復の実装を学びたい
- DockerでマルチテナントAIエージェントを提供したい

## やり方

1. MCPサーバーをstdioまたはHTTPで起動 2. JSON-RPCで`tools/list`リクエストを送信してツール一覧取得 3. `tools/call`でツールを実行 4. エージェント側でMCPツールを通常ツールと同様に扱う 5. 設定ファイルでMCPサーバーを追加すればホットリロード可能

### 入力

- MCPサーバー（stdio/HTTP）
- MCP設定ファイル（JSON）

### 出力

- 再起動不要のツール追加
- 外部システムとのプラグイン連携
- ホットリロード可能なツールセット

## 使うツール・ライブラリ

- MCP（Model Context Protocol）
- websocket-client（HTTP MCP用）

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
