# cron自然言語スケジューリングとプラットフォーム配信

> 自然言語でスケジュールタスク（日次レポート、夜間バックアップ、週次監査等）を定義し、任意のメッセージングプラットフォームへ結果を配信する

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

従来のcronは手動で複雑なスクリプトを書く必要があり、結果を好きなチャネルへ配信する仕組みが別途必要。Hermesの組み込みcronなら自然言語でタスクを定義し、Telegram等へ自動配信できる

## いつ使うのか

定期的な自動化タスク（日次レポート、バックアップ、監査、通知等）を自然言語で設定したいとき

## やり方

1. `hermes`で会話を開始
2. `/cron`コマンドでスケジュールを定義（例: `毎日9時にGitHub issue summaryをTelegramへ送信`）
3. エージェントがcron設定を自動生成
4. 指定時刻になるとタスクが無人実行され、結果が指定プラットフォームへ配信される
5. `/cron list`で登録済みタスク確認、`/cron delete`で削除可能

### 入力

- 自然言語スケジュール定義
- 配信先プラットフォーム

### 出力

- 無人実行タスク
- 指定プラットフォームへの結果配信

## 使うツール・ライブラリ

- Hermes cron scheduler
- メッセージングゲートウェイ

## 前提知識

- Linux/macOS/WSL2環境（Windows nativeは非対応）
- git
- LLMプロバイダーAPIキー（OpenRouter/OpenAI/Anthropic/Kimi/MiniMax等のいずれか）
- Python 3.11+ (インストーラーが自動セットアップ)
- Node.js (インストーラーが自動セットアップ)
- Telegram/Discord等のBot Token（メッセージングゲートウェイ利用時）
- Daytona/Modalアカウント（サーバーレス利用時、オプション）
