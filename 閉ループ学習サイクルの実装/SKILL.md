# 閉ループ学習サイクルの実装

> エージェントが会話・タスク実行から自律的にスキルを生成し、実行中に改善し、メモリとユーザーモデルを更新し続ける仕組み

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

一度きりの応答ではなく、使うほど賢くなるエージェントを実現するため。過去の経験を検索・活用することで、文脈の一貫性と品質が向上する。

## いつ使うのか

長期的に育てるAIアシスタントを設計する際、会話履歴を活かして応答品質を向上させたい場合

## やり方

1. 複雑なタスク実行後、自律的にスキルを生成 2. スキル実行中に自己改善ロジックを適用 3. FTS5による全文検索で過去会話をLLM要約して参照 4. Honcho dialecticでユーザーモデルを継続更新 5. agentskills.io標準に準拠してスキル共有

### 入力

- タスク実行履歴
- 過去会話ログ（SQLite FTS5検索可能）
- ユーザー対話データ（Honcho）

### 出力

- 自動生成スキル（agentskills.io互換）
- 改善されたスキル実行結果
- ユーザーモデル（好み・文脈理解）

## 使うツール・ライブラリ

- SQLite FTS5
- Honcho（plastic-labs）
- agentskills.io標準

## 前提知識

- 基本的なコマンドライン操作
- LLM APIキー（OpenRouter/OpenAI/Anthropic等のいずれか）
- gitがインストールされた環境
- Linux/macOS/WSL2のいずれか
