# ビルド後に自動デモ動画を生成しPRに添付する

> AIエージェントが何かをビルドするたびに、自動で画面録画によるデモ動画を生成し、PRに添付するワークフローを構築する。

- 出典: https://x.com/AlexFinn/status/2026515546695754195
- 投稿者: Alex Finn
- カテゴリ: agent-orchestration

## なぜ使うのか

PRレビュアーがコードを読まずに実装の動作を視覚的に確認できるため、レビュー効率が向上する。またAIエージェント自身が動作確認を兼ねてデモを記録するため、バグの早期発見にもつながる。

## いつ使うのか

AIエージェントが自律的にコードをビルド・コミット・PR作成するワークフローを運用しており、PRレビューの視認性を高めたい場合。

### 具体的な適用場面

- 既存SaaSツールの特定機能だけが欲しいが、月額費用を払いたくない場合
- 新しいSaaS機能発表を見て「自分のワークフローに取り込みたい」と思った場合
- PRレビュー時に実装内容をビデオで確認させたい開発チームのワークフロー構築

## やり方

投稿には具体的な実装コードは示されていない。概念的な流れは以下の通り:
1. AIエージェントがタスク完了後のフックとして画面録画ツール（例: ffmpeg + xvfb、Electron ScreenCapture API等）を起動
2. 実装された機能を自動操作して動作デモを録画
3. 動画ファイルをPR作成時に添付（GitHub Actions経由でアーティファクトとして添付、またはコメントに埋め込み）

なお本投稿では実装詳細は公開されておらず、「Cursorの発表文をOpenClawに渡したら5分で動いた」とのみ述べられている。具体的な実装方法は別途調査が必要。

### 入力

- AIエージェントが完成させたビルド成果物
- 画面録画ツール
- GitHub等のPRシステムへのアクセス

### 出力

- PRに添付されたデモ動画ファイル
- 実装の動作を視覚的に確認できる証跡

## 使うツール・ライブラリ

- OpenClaw（パーソナルAIエージェント）
- GitHub（PR添付先）

## 前提知識

- OpenClaw等のパーソナルAIエージェント環境が稼働していること
- エージェントがコード実装からPR作成まで自律的に実行できるワークフローが構築済みであること
- 画面録画を自動起動できる環境（macOS/Linux）

## 根拠

> 「I pasted in the announcement to Henry. He said on it chief. 5 minutes later he not only built out the entire feature, but recorded a demo video of it too」

> 「It's now implemented into our entire workflow. Now every time I ask my OpenClaw to build something, a demo video will be attached to every PR」

> 「Their AI agent records demo videos of itself after it builds things」（Cursorの機能説明）
