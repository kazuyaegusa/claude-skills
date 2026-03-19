# OpenClawからの自動マイグレーション

> OpenClawの設定・メモリ・スキル・APIキーをHermes Agentへ自動インポートする

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: claude-code-workflow

## なぜ使うのか

OpenClawユーザーが手動で全設定を移行するのは時間がかかり、ミスが起きやすい。自動マイグレーションなら、ペルソナ・記憶・スキル・シークレットまで一括で移行できる

## いつ使うのか

OpenClawからHermes Agentへ移行するとき

## やり方

1. Hermes Agent初回セットアップ時、`hermes setup`が自動で`~/.openclaw`を検出してマイグレーションを提案
2. または、インストール後いつでも`hermes claw migrate`を実行
3. `--dry-run`でプレビュー可能
4. `--preset user-data`でシークレットを除外してマイグレート
5. SOUL.md（ペルソナ）、MEMORY.md/USER.md（記憶）、スキル、コマンド許可リスト、メッセージング設定、APIキー、TTS音声ファイル、AGENTS.md等が自動インポートされる

### 入力

- ~/.openclawディレクトリ

### 出力

- Hermes Agentへインポートされた設定・記憶・スキル・シークレット

## 使うツール・ライブラリ

- hermes claw migrate

## コード例

```
hermes claw migrate              # Interactive migration
hermes claw migrate --dry-run    # Preview
hermes claw migrate --preset user-data   # Without secrets
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

> 「curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash」

> 「Works on Linux, macOS, and WSL2. The installer handles everything — Python, Node.js, dependencies, and the `hermes` command. No prerequisites except git.」

> 「hermes claw migrate — Interactive migration (full preset) / hermes claw migrate --dry-run — Preview what would be migrated」
