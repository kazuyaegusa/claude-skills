# 機能発表文を仕様書としてAIに実装させる

> 競合SaaSやOSSの機能発表・ブログ・ツイートのテキストを、そのままAIエージェントへの実装指示として渡し、同等機能を自前実装する。

- 出典: https://x.com/AlexFinn/status/2026515546695754195
- 投稿者: Alex Finn
- カテゴリ: agent-orchestration

## なぜ使うのか

機能発表文には「何ができるか」「ユーザーにとってどう見えるか」が凝縮されており、AIエージェントが実装に必要な仕様を十分に読み取れる。高額SaaS契約なしに同等の機能を数分で手に入れられる。

## いつ使うのか

SaaSの新機能発表を見て「これを自分のワークフローに取り込みたい」と思ったとき。特に機能説明が十分に具体的で、外部依存が少ない機能に有効。

### 具体的な適用場面

- 既存SaaSツールの特定機能だけが欲しいが、月額費用を払いたくない場合
- 新しいSaaS機能発表を見て「自分のワークフローに取り込みたい」と思った場合
- PRレビュー時に実装内容をビデオで確認させたい開発チームのワークフロー構築

## やり方

1. 対象SaaSの機能発表文（ブログ記事、公式ツイート、プレスリリース等）をコピー
2. 自前のAIエージェント（OpenClaw等）のチャットに貼り付ける
3. 「これを実装して」等の指示を付けて送信
4. エージェントが要件を解析して実装・動作確認まで完了させる

例: Cursorの発表文（「AIエージェントがビルド後にデモ動画を録画する」）をそのままOpenClawに貼った → 5分後に動作する実装が完成

### 入力

- 機能発表テキスト（ブログ、ツイート、プレスリリース等）
- 自前のAIエージェント環境（OpenClaw等）

### 出力

- 発表された機能と同等の動作をする実装コード
- 自分のワークフローに組み込まれた機能

## 使うツール・ライブラリ

- OpenClaw（パーソナルAIエージェント）

## 前提知識

- OpenClaw等のパーソナルAIエージェント環境が稼働していること
- エージェントがコード実装からPR作成まで自律的に実行できるワークフローが構築済みであること
- 画面録画を自動起動できる環境（macOS/Linux）

## 根拠

> 「I pasted in the announcement to Henry. He said on it chief. 5 minutes later he not only built out the entire feature, but recorded a demo video of it too」

> 「It's now implemented into our entire workflow. Now every time I ask my OpenClaw to build something, a demo video will be attached to every PR」

> 「Their AI agent records demo videos of itself after it builds things」（Cursorの機能説明）
