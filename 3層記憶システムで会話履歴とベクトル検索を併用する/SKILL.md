# 3層記憶システムで会話履歴とベクトル検索を併用する

> セッション履歴・LLM圧縮長期記憶・LanceDBベクトル検索の3層で記憶を管理し、文脈を保持しながら関連情報を取り出す

- 出典: https://x.com/qingq77/status/2035241244289638417
- 投稿者: Geek Lite
- カテゴリ: agent-orchestration

## なぜ使うのか

会話履歴だけではトークン制限で長期記憶が不可能。全てをベクトル検索にすると直近の文脈が失われる。3層構造で両立する

## いつ使うのか

長期間運用するエージェントで、過去の会話内容を参照しながら応答したい時

### 具体的な適用場面

- 既存フレームワークの抽象化に不満があり、エージェントの挙動を完全制御したい
- 依存関係を最小化した本番運用可能なAIエージェントを構築したい
- Tool Use・記憶・自己修復の実装を学びたい
- DockerでマルチテナントAIエージェントを提供したい

## やり方

1. セッション中は会話履歴をメモリに保持 2. 定期的にLLMで要約・圧縮して長期記憶として保存 3. 長期記憶をLanceDBにベクトル化して格納 4. クエリ時にベクトル検索で関連記憶を取得し、会話履歴に注入

### 入力

- 会話履歴（セッション）
- LLM要約API
- LanceDB（ベクトルDB）

### 出力

- トークン制限内で長期記憶を参照可能
- 関連する過去情報の自動取得
- セッション再起動後も文脈維持

## 使うツール・ライブラリ

- LanceDB（ベクトルDB）
- OpenAI API（要約用）

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
