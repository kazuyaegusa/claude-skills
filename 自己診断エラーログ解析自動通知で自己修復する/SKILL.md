# 自己診断・エラーログ解析・自動通知で自己修復する

> 日次セルフチェック、セッション健全性診断、エラーログ解析を実行し、異常検出時に自動通知・修復を試みる

- 出典: https://x.com/qingq77/status/2035241244289638417
- 投稿者: Geek Lite
- カテゴリ: agent-orchestration

## なぜ使うのか

24/7運用では人間が常時監視できない。エージェント自身が健全性をチェックし、異常を検知・通報・修復すれば無人運用が可能になる

## いつ使うのか

本番環境で24/7運用するエージェントに、無人監視・自己修復機能を持たせたい時

### 具体的な適用場面

- 既存フレームワークの抽象化に不満があり、エージェントの挙動を完全制御したい
- 依存関係を最小化した本番運用可能なAIエージェントを構築したい
- Tool Use・記憶・自己修復の実装を学びたい
- DockerでマルチテナントAIエージェントを提供したい

## やり方

1. 日次cronで`self_check`ツールを実行 2. メモリ使用量・ディスク容量・プロセス状態を確認 3. エラーログをLLMで解析して原因を推定 4. 異常検出時に企業微信/Slack等に通知 5. 可能なら自動修復（プロセス再起動、一時ファイル削除等）を試行

### 入力

- システムメトリクス（メモリ・CPU・ディスク）
- エラーログ
- 通知先API（WeChat Work/Slack等）

### 出力

- 日次健全性レポート
- 異常検知時の即時通知
- 自動修復の試行

## 使うツール・ライブラリ

- croniter（スケジューリング）
- psutil（システムメトリクス）
- WeChat Work API

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
