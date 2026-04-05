# 並列サブエージェント＋RPC統合によるコンテキストコスト削減

> 独立したサブエージェントを並列生成し、PythonスクリプトからツールをRPC呼び出しすることで、マルチステップパイプラインをゼロコンテキストコストで実行する

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

全タスクをメインエージェントで逐次実行するとコンテキストが肥大化し、コスト増＋応答遅延が発生する。サブエージェントで並列化し、スクリプトでツール呼び出しをラップすることで、LLM呼び出し回数を大幅削減できる

## いつ使うのか

並列処理可能なタスクがある、コンテキストウィンドウを節約したい、複雑なパイプラインを効率化したい場合

## やり方

1. サブエージェント生成API（spawn isolated subagent）を実装
2. 並列ワークストリーム用に複数サブエージェントを起動
3. Pythonスクリプト内でツールをRPC経由で呼び出せるようにする（tool-calling via RPC）
4. マルチステップパイプラインをスクリプトにまとめ、1ターンで実行
5. サブエージェント完了後に結果を集約してメインエージェントに返す

### 入力

- サブエージェント用タスク定義
- RPC呼び出し用Pythonスクリプト

### 出力

- 並列実行結果
- 削減されたLLM呼び出し回数・コンテキストサイズ

## 使うツール・ライブラリ

- RPC（詳細不明だが、おそらくgRPC/JSON-RPC等）
- Python

## 前提知識

- Linux/macOS/WSL2環境（WindowsネイティブはWSL2必須）
- git（インストールスクリプトの唯一の前提条件）
- LLMプロバイダーのAPIキー（Anthropic, OpenRouter, OpenAI等）
- （オプション）メッセージングプラットフォームのBot認証トークン
- （オプション）SSH/Daytona/Modal等のバックエンド認証情報

## 根拠

> "Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns."
