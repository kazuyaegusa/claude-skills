# ffmpeg + APIでトリミング・BGM追加・AI動画生成をツール化する

> ffmpegで動画トリミング・BGM追加を実行し、AI動画生成APIを呼び出すツールをエージェントに提供する

- 出典: https://x.com/qingq77/status/2035241244289638417
- 投稿者: Geek Lite
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントがマルチモーダルタスク（動画編集・生成）を実行できれば、用途が大幅に広がる

## いつ使うのか

エージェントに動画編集・生成機能を持たせたい時

### 具体的な適用場面

- 既存フレームワークの抽象化に不満があり、エージェントの挙動を完全制御したい
- 依存関係を最小化した本番運用可能なAIエージェントを構築したい
- Tool Use・記憶・自己修復の実装を学びたい
- DockerでマルチテナントAIエージェントを提供したい

## やり方

1. `ffmpeg -i input.mp4 -ss 00:00:10 -t 00:00:30 output.mp4`でトリミング 2. `ffmpeg -i video.mp4 -i bgm.mp3 -filter_complex amerge output.mp4`でBGM追加 3. AI動画生成APIを呼び出してプロンプトから動画生成 4. これらをツール関数としてエージェントに公開

### 入力

- 動画ファイル
- BGMファイル
- プロンプト（AI生成用）

### 出力

- 編集済み動画
- AI生成動画

## 使うツール・ライブラリ

- ffmpeg
- AI動画生成API（例: Runway, Pika）

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
