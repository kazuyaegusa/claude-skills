# croniterで永続的な定時タスク・単発タスクを管理する

> cron式で定期実行タスクを定義し、再起動後も永続化されたスケジュールで実行を継続する

- 出典: https://x.com/qingq77/status/2035241244289638417
- 投稿者: Geek Lite
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントが定期的に実行すべきタスク（自己診断、データ収集等）がある。再起動で消えない永続化されたスケジューラが必要

## いつ使うのか

エージェントに定期実行タスクを持たせたい、かつ再起動後もスケジュールを維持したい時

### 具体的な適用場面

- 既存フレームワークの抽象化に不満があり、エージェントの挙動を完全制御したい
- 依存関係を最小化した本番運用可能なAIエージェントを構築したい
- Tool Use・記憶・自己修復の実装を学びたい
- DockerでマルチテナントAIエージェントを提供したい

## やり方

1. `croniter`でcron式を解析 2. タスク定義をJSONファイルに保存 3. 起動時にJSONを読み込んで次回実行時刻を計算 4. メインループで時刻をチェックし、該当タスクを実行 5. 単発タスクは実行後に削除、定期タスクは次回時刻を更新

### 入力

- cron式（例: `0 2 * * *`）
- タスク定義（ツール名・引数）

### 出力

- 定期実行タスク
- 単発タスク
- 再起動後も継続するスケジュール

## 使うツール・ライブラリ

- croniter

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
