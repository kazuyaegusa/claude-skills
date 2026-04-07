# サーバーレス永続化バックエンド

> Daytona/Modalを使い、アイドル時は休止、必要時のみ起動してコストをほぼゼロに抑える永続環境

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

常時稼働するVMはコストが高い。サーバーレス永続化なら、使わない間は課金されず、必要時に即座に復帰できる。

## いつ使うのか

エージェントを常駐させたいがコストを抑えたい場合、$5 VPSやGPUクラスタで柔軟に動かしたい場合

## やり方

1. `hermes config set terminal.backend daytona`または`modal`を設定 2. アイドル時は環境が自動休止 3. メッセージ受信で自動ウェイクアップ 4. セッション状態は永続化されるため、文脈を引き継ぐ

### 入力

- Daytona/Modal設定

### 出力

- アイドル時コストほぼゼロの永続環境
- 即座に復帰するセッション

## 使うツール・ライブラリ

- Daytona
- Modal

## コード例

```
hermes config set terminal.backend daytona
```

## 前提知識

- 基本的なコマンドライン操作
- LLM APIキー（OpenRouter/OpenAI/Anthropic等のいずれか）
- gitがインストールされた環境
- Linux/macOS/WSL2のいずれか

## 根拠

> Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in.
