# モデルプロバイダー非依存設計

> LLMプロバイダーを `hermes model` コマンドで切り替え可能にし、コード変更なしで200+モデルを利用可能にする

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

特定プロバイダーにロックインされると、コスト・パフォーマンス・可用性のトレードオフができない。抽象化することで、実験・本番・フォールバックでモデルを柔軟に切り替えられる

## いつ使うのか

プロバイダー依存を避けたい、複数モデルを試したい、コスト最適化したい、特定地域のモデル（中国のGLM/Kimi等）を使いたい場合

## やり方

1. モデルプロバイダーを抽象化（Nous Portal, OpenRouter, OpenAI, Anthropic, z.ai/GLM, Kimi/Moonshot, MiniMax等）
2. `hermes model` でプロバイダー:モデルを指定
3. 設定ファイルにAPIキーを保存
4. エージェント実行時に指定されたプロバイダーのAPIを呼び出し
5. OpenRouterを使えば200+モデルに単一APIでアクセス可能

### 入力

- プロバイダー名とモデル名
- APIキー

### 出力

- コード変更なしでモデル切り替え可能なエージェント

## 使うツール・ライブラリ

- OpenRouter（200+モデル統合API）
- Nous Portal
- OpenAI API
- Anthropic API
- z.ai/GLM
- Kimi/Moonshot
- MiniMax

## コード例

```
hermes model
# または
/model openrouter:anthropic/claude-3.5-sonnet
/model openai:gpt-4-turbo
```

## 前提知識

- Linux/macOS/WSL2環境（WindowsネイティブはWSL2必須）
- git（インストールスクリプトの唯一の前提条件）
- LLMプロバイダーのAPIキー（Anthropic, OpenRouter, OpenAI等）
- （オプション）メッセージングプラットフォームのBot認証トークン
- （オプション）SSH/Daytona/Modal等のバックエンド認証情報

## 根拠

> "Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in."
