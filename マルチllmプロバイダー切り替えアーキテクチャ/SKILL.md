# マルチLLMプロバイダー切り替えアーキテクチャ

> `hermes model`コマンドで、コード変更なしに200+モデル（OpenRouter、z.ai/GLM、Kimi/Moonshot、MiniMax、OpenAI等）を瞬時に切り替え可能にする

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

特定のLLMプロバイダーやモデルにロックインされると、価格変動・API障害・モデル性能差に柔軟に対応できない。プロバイダー非依存のアーキテクチャなら、最適なモデルを自由に選択でき、コストと性能を最大化できる

## いつ使うのか

複数LLMプロバイダーを試したいとき、コスト最適化のためモデルを切り替えたいとき、特定APIの障害時にフォールバック先を確保したいとき

## やり方

1. インストール後、`hermes model`を実行
2. プロバイダー（Nous Portal, OpenRouter, z.ai, Kimi, MiniMax, OpenAI等）を選択
3. モデルIDを選択（OpenRouterなら200+モデルから選択）
4. 設定が自動で保存され、以降の会話で選択したモデルが使用される
5. いつでも`hermes model`で別モデルへ切り替え可能（コード変更不要）

### 入力

- LLMプロバイダーAPIキー
- モデルID

### 出力

- コード変更なしのモデル切り替え
- 統一インターフェースで200+モデル利用可能

## 使うツール・ライブラリ

- OpenRouter
- Nous Portal
- z.ai/GLM
- Kimi/Moonshot
- MiniMax
- OpenAI

## コード例

```
hermes model
# Interactive selection → instant switch, no code change
```

## 前提知識

- Linux/macOS/WSL2環境（Windows nativeは非対応）
- git
- LLMプロバイダーAPIキー（OpenRouter/OpenAI/Anthropic/Kimi/MiniMax等のいずれか）
- Python 3.11+ (インストーラーが自動セットアップ)
- Node.js (インストーラーが自動セットアップ)
- Telegram/Discord等のBot Token（メッセージングゲートウェイ利用時）
- Daytona/Modalアカウント（サーバーレス利用時、オプション）

## 根拠

> 「Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in.」

> 「Works on Linux, macOS, and WSL2. The installer handles everything — Python, Node.js, dependencies, and the `hermes` command. No prerequisites except git.」
