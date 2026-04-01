# ECCをnpxで一括導入する

> 125+のスキル・60+スラッシュコマンド・28専門サブエージェントをnpx ecc-universalコマンド1本でClaude Code環境に追加する

- 出典: https://x.com/l_go_mrk/status/2037489559186145787
- 投稿者: AI駆動塾
- カテゴリ: claude-code-workflow

## なぜ使うのか

個別インストールでは各スキルのダウンロード・設定ファイル配置を手動で繰り返す必要があるが、ecc-universalはそれを一括で行い、すぐに本番同等の拡張済みClaude Code環境を得られる

## いつ使うのか

Claude Codeを新しいマシンに導入したとき、またはプロジェクトでClaude Codeの能力を最大化した状態から始めたいとき

### 具体的な適用場面

- 新規プロジェクト立ち上げ時に、Claude Codeの能力を最大化した状態でスタートしたいとき
- 既存プロジェクトに対して脆弱性チェックを自動化したいとき（OWASP等102ルール）
- フロントエンド・バックエンド・テスト・セキュリティ等を同時進行で進めたいマルチドメインタスクのとき

## やり方

1. Node.js環境でターミナルを開く
2. `npx ecc-universal` を実行（インストーラーが~/.claude/以下にskills/commands/agentsを配置）
3. Claude Codeを再起動してスキルが反映されたことを確認
4. `/help` でインストール済み60+コマンドが一覧表示される

### 入力

- Node.js（npx実行可能な環境）
- Claude Code CLI インストール済み

### 出力

- ~/.claude/skills/ 以下に125+スキルファイルが配置される
- ~/.claude/commands/ 以下に60+スラッシュコマンドが配置される
- CLAUDE.md に28専門サブエージェントのエントリーが追記される

## 使うツール・ライブラリ

- ecc-universal（npm package）
- Claude Code CLI

## コード例

```
npx ecc-universal
```

## 前提知識

- Claude Code CLIのインストール（npm install -g @anthropic-ai/claude-code または brew install claude）
- Node.js v18以上（npx実行のため）
- Claude ProまたはMax サブスクリプション（サブエージェント並列実行にはトークン消費が多い）

## 根拠

> 「28の専門サブエージェントが連携して動く」（投稿本文）

> 「125以上のSkillsをプリビルドで搭載」（投稿本文）

> 「60以上のスラッシュコマンド」（投稿本文）

> 「セキュリティスキャン内蔵（102ルール、1,282テスト）」（投稿本文）

> 「Anthropicハッカソンで優勝した」（投稿本文）
