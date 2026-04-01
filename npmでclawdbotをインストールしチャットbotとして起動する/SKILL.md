# npmでClawdBotをインストールし、チャットBotとして起動する

> npm経由でClawdBotをインストールし、Discord/Slack/TelegramのBotトークンを設定してAIエージェントをチャット経由で操作可能にする

- 出典: https://x.com/ai_masaou/status/2014624157112402078
- 投稿者: まさお@AI駆動開発
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeのターミナル操作に慣れていないユーザーや、既存のチャットワークフローを崩したくない場合でも、同等の機能を利用できるため

## いつ使うのか

Discord/Slackを主要なコミュニケーション手段としており、そこからAI支援を受けたい場合

### 具体的な適用場面

- Discord/Slackでチーム作業中にAI支援が必要な場面
- 複数日にまたがるプロジェクトで文脈を引き継ぎたい場合
- ハンズフリーで音声指示を出しながらPC作業を進めたい場面
- 既存のチャットワークフローにAI機能を統合したい組織
- ブラウザ自動操作・情報収集・フォーム入力を定期的に行う業務

## やり方

1. `npm install -g clawd-bot` (または同等のインストールコマンド) 2. インストール後のオンボーディングでモデル(Claude/GPT等)を選択 3. Discord/Slack/TelegramのBotトークンを設定ファイルに記載 4. 必要なスキル(ブラウザ操作、音声認識、FFmpeg等)を選択 5. チャットアプリからBotにメンションして対話開始

### 入力

- npm実行環境
- Discord/Slack/TelegramのBotトークン
- Anthropic APIキー(Claude利用時)

### 出力

- チャットアプリから操作可能なAIエージェント
- ブラウザ自動操作・資料生成・音声文字起こし等の実行結果

## 使うツール・ライブラリ

- ClawdBot
- npm
- Discord/Slack/Telegram API

## 前提知識

- Node.js/npm実行環境
- Discord/Slack/TelegramのBot作成・トークン取得方法
- Anthropic APIキーの取得方法
- 基本的なコマンドライン操作
- Claude Codeまたは同等のAIエージェントツールの概念理解

## 根拠

> 「npmコマンド一発でインストール完了」

> 「DiscordやSlack、Telegramから指示を出す」

> 「フック設定でセッションログを保存」「メモリディレクトリに情報を蓄積」「昨日の続きで」と言えば文脈を引き継げる

> 「2025年12月21日時点では1000スター未満」「2026年1月10日頃には2000スター」「そこからJカーブで急上昇」

> 「2026年1月上旬にAnthropicがClaude認証の意図せぬ利用を規制」「現在はAPIキー経由での利用が推奨」
