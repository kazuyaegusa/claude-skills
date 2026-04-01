# 企業微信でデバウンス・メッセージ分割・メディア処理を実装する

> 企業微信（WeChat Work）でメッセージ受信時のデバウンス処理、長文の自動分割、画像・動画・音声・ファイルのアップロード/ダウンロードを実装する

- 出典: https://x.com/qingq77/status/2035241244289638417
- 投稿者: Geek Lite
- カテゴリ: agent-orchestration

## なぜ使うのか

短時間に複数メッセージが来ると重複処理が発生する。長文はAPIの制限で分割が必要。メディアはアップロード/ダウンロードAPIが別途必要

## いつ使うのか

企業微信をエージェントのインターフェースとして使い、実用的なメッセージ処理とメディア対応を実装したい時

### 具体的な適用場面

- 既存フレームワークの抽象化に不満があり、エージェントの挙動を完全制御したい
- 依存関係を最小化した本番運用可能なAIエージェントを構築したい
- Tool Use・記憶・自己修復の実装を学びたい
- DockerでマルチテナントAIエージェントを提供したい

## やり方

1. メッセージ受信時に1秒間デバウンス（同一ユーザーからの連続メッセージをまとめる） 2. 返信が2048文字を超える場合は分割して複数メッセージで送信 3. 画像・動画・音声・ファイルは`media/upload`でアップロード、`media/get`でダウンロード 4. メディアIDを管理してエージェントに渡す

### 入力

- 企業微信Webhook
- 企業微信API Key
- メディアファイル

### 出力

- デバウンス済みメッセージ
- 分割送信された長文
- アップロード/ダウンロードされたメディア

## 使うツール・ライブラリ

- 企業微信API（WeChat Work）

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
