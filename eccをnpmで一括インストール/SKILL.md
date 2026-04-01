# ECCをnpmで一括インストール

> npxコマンド一行でEverything Claude Codeの125+スキル・28サブエージェント・60+スラッシュコマンドをClaude Codeに追加する

- 出典: https://x.com/l_go_mrk/status/2037489559186145787
- 投稿者: AI駆動塾
- カテゴリ: claude-code-workflow

## なぜ使うのか

Anthropicハッカソン優勝時点で検証済みの構成をそのまま使うことで、ゼロから個別スキルを集める数週間のセットアップを省略できる

## いつ使うのか

新規プロジェクトのセットアップ時、またはClaude Codeのデフォルト構成では対応困難な複合タスクが頻発している時

### 具体的な適用場面

- 新規プロジェクト開始時にClaude Codeのデフォルト能力をゼロから拡張したい場合
- PRマージ前・本番リリース前に多言語コードベースを横断してセキュリティ脆弱性を自動検出したい場合
- コード生成・テスト・セキュリティレビューを同一セッション内で並列処理したい場合

## やり方

1. `npx ecc-universal` を実行（グローバルインストール不要）
2. または GitHub App「ecc-tools」をGitHub Marketplaceからインストール（150+インストール実績あり）
3. インストール後、`/python-patterns`・`/security-scan`・`/tdd`・`/brainstorm` 等のスラッシュコマンドが利用可能になる
4. `claude skills list` で導入済みスキル一覧を確認

### 入力

- Node.js環境（npx実行のため）
- Claude Code CLIが設定済みの環境

### 出力

- 125以上のプリビルドスキルが ~/.claude/skills/ に配備された状態
- 60以上のスラッシュコマンドが利用可能な状態
- 28専門サブエージェントが設定された状態

## 使うツール・ライブラリ

- npx
- ecc-universal (npm package)
- ecc-tools (GitHub App)
- Claude Code CLI

## コード例

```
npx ecc-universal
```

## 前提知識

- Claude Code CLIがインストールされていること（`claude --version` で確認）
- Node.js / npxが使用可能な環境（ecc-universal/ecc-agentshieldのインストールに必要）
- GitHubアカウント（GitHub App経由のインストールを使う場合）

## 根拠

> 28の専門サブエージェントが連携して動く

> 125以上のSkillsをプリビルドで搭載

> 60以上のスラッシュコマンド

> セキュリティスキャン内蔵（102ルール、1,282テスト）

> 7言語対応
