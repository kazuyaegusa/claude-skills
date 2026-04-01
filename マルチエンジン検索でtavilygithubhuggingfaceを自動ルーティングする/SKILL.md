# マルチエンジン検索でTavily/GitHub/HuggingFaceを自動ルーティングする

> 検索クエリに応じてTavily（Web検索）・GitHub（コード検索）・HuggingFace（モデル検索）を自動選択して実行する

- 出典: https://x.com/qingq77/status/2035241244289638417
- 投稿者: Geek Lite
- カテゴリ: agent-orchestration

## なぜ使うのか

単一検索エンジンでは不足する。クエリの意図に応じて最適なエンジンを選択すれば、回答精度が向上する

## いつ使うのか

エージェントに多様な情報源から検索させたい、かつクエリに応じて最適なエンジンを選択したい時

### 具体的な適用場面

- 既存フレームワークの抽象化に不満があり、エージェントの挙動を完全制御したい
- 依存関係を最小化した本番運用可能なAIエージェントを構築したい
- Tool Use・記憶・自己修復の実装を学びたい
- DockerでマルチテナントAIエージェントを提供したい

## やり方

1. 検索クエリをLLMで分類（Web情報/コード/モデル） 2. 分類結果に基づいてTavily/GitHub/HuggingFace APIを呼び出し 3. 結果を統合して返す 4. ツール定義で`search`として公開し、エージェントが透過的に使用

### 入力

- 検索クエリ
- Tavily API Key
- GitHub API Key
- HuggingFace API Key

### 出力

- 最適エンジンによる検索結果
- 自動ルーティング機構

## 使うツール・ライブラリ

- Tavily API
- GitHub API
- HuggingFace API

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
