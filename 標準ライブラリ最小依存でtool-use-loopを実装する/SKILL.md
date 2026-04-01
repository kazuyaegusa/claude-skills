# 標準ライブラリ+最小依存でTool Use Loopを実装する

> OpenAI互換のFunction Callingを標準ライブラリで実装し、自動リトライ・最大20イテレーションのループを実現する

- 出典: https://x.com/qingq77/status/2035241244289638417
- 投稿者: Geek Lite
- カテゴリ: agent-orchestration

## なぜ使うのか

LangChainなどのフレームワークはオーバーヘッドが大きく、ループ制御やエラーハンドリングが隠蔽される。標準ライブラリで書けば挙動を完全制御でき、依存地獄を回避できる

## いつ使うのか

エージェントのツール呼び出しループを自前で実装したい、かつフレームワークの抽象化を避けたい時

### 具体的な適用場面

- 既存フレームワークの抽象化に不満があり、エージェントの挙動を完全制御したい
- 依存関係を最小化した本番運用可能なAIエージェントを構築したい
- Tool Use・記憶・自己修復の実装を学びたい
- DockerでマルチテナントAIエージェントを提供したい

## やり方

1. `requests`でOpenAI互換APIを直接呼び出し 2. レスポンスから`tool_calls`を抽出 3. 各ツールをPython関数として実装し、名前で動的に呼び出す 4. 結果を次のAPI呼び出しに含めてループ 5. `max_iterations=20`で打ち切り条件を設定

### 入力

- OpenAI互換APIエンドポイント
- ツール定義（JSON Schema形式）
- ツール実装（Python関数）

### 出力

- 最大20イテレーションのTool Useループ
- 自動リトライ機構
- 完全に制御可能なエージェント挙動

## 使うツール・ライブラリ

- Python標準ライブラリ
- requests（HTTPクライアント）

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
