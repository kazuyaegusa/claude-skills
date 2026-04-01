# create_toolでランタイム中にツールを生成・保存・ロードする

> エージェント実行中にPythonコードでツールを書き、ファイルに保存し、次回起動時に自動ロードする自己拡張機構

- 出典: https://x.com/qingq77/status/2035241244289638417
- 投稿者: Geek Lite
- カテゴリ: agent-orchestration

## なぜ使うのか

事前定義したツールだけでは不足する場合がある。エージェント自身が必要なツールを生成できれば、柔軟性が大幅に向上する

## いつ使うのか

エージェントが自律的にツールセットを拡張する必要がある時、または運用中に新しいツールが必要になった時

### 具体的な適用場面

- 既存フレームワークの抽象化に不満があり、エージェントの挙動を完全制御したい
- 依存関係を最小化した本番運用可能なAIエージェントを構築したい
- Tool Use・記憶・自己修復の実装を学びたい
- DockerでマルチテナントAIエージェントを提供したい

## やり方

1. `create_tool`ツールをエージェントに提供 2. エージェントがPythonコードでツール実装を生成 3. `tools/`ディレクトリに`.py`ファイルとして保存 4. 起動時に`tools/`内の`.py`を動的インポート 5. ツール定義JSONも自動生成してAPI呼び出しに含める

### 入力

- ツール名・説明・パラメータ定義
- ツール実装のPythonコード

### 出力

- 実行時に生成されたツール
- 永続化されたツールファイル
- 次回起動時の自動ロード

## 使うツール・ライブラリ

- Python標準ライブラリ（importlib）

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
