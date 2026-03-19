# サーバーレス永続化ターミナルバックエンドの利用

> エージェントの実行環境をDaytona/Modalといったサーバーレスバックエンドで動かし、アイドル時に休止・オンデマンド起動することでコストをほぼゼロに抑えつつ、ラップトップから切り離して24/7アクセス可能にする

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

ローカルマシンに縛られるとラップトップを閉じた瞬間にエージェントが止まる。サーバーレス環境なら、使わない時間帯はコストゼロで休止し、メッセージが来た瞬間に起動するため、コストとアクセシビリティの両立が可能

## いつ使うのか

$5 VPSやGPUクラスターで24/7稼働させたいが、アイドル時のコストを最小化したいとき。どこからでもアクセスしたいとき

## やり方

1. Hermes Agentインストール後、`hermes setup`で環境バックエンドを選択
2. Daytona または Modal を選択
3. 環境が自動でセットアップされ、アイドル時に休止
4. Telegram/Discord等からメッセージを送ると環境が自動起動
5. タスク完了後、再び休止してコスト削減
6. 6種類のターミナルバックエンド（local, Docker, SSH, Daytona, Singularity, Modal）から選択可能

### 入力

- Daytona または Modal アカウント
- Hermes Agent設定

### 出力

- 休止可能な永続エージェント環境
- オンデマンド起動
- アイドル時コストほぼゼロ

## 使うツール・ライブラリ

- Daytona
- Modal
- Hermes Agent terminal backends

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

> 「Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions.」

> 「curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash」

> 「Works on Linux, macOS, and WSL2. The installer handles everything — Python, Node.js, dependencies, and the `hermes` command. No prerequisites except git.」

> 「hermes claw migrate — Interactive migration (full preset) / hermes claw migrate --dry-run — Preview what would be migrated」
