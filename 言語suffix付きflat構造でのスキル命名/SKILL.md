# 言語suffix付きFlat構造でのスキル命名

> スキル名を `azure-<service>-<language>` 形式（例: `azure-ai-projects-py`）で統一し、`.github/skills/` 直下にフラット配置する

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

エージェントが言語を自動判別してスキルを検索しやすくし、階層的なディレクトリ構造による複雑性を回避する

## いつ使うのか

多言語対応のスキルカタログを構築し、エージェントが言語を自動判別して適切なスキルをロードする必要がある場合

## やり方

1. スキル名を `<domain>-<service>-<lang-suffix>` で定義（py/dotnet/ts/java/rust） 2. `.github/skills/<skill-name>/SKILL.md` に配置 3. `skills/<language>/<category>/` からSymlinkで参照

### 入力

- 対象SDK/サービス名
- 対応言語
- カテゴリ（foundry/data/messaging等）

### 出力

- .github/skills/<skill-name>/SKILL.md
- skills/<language>/<category>/<alias> へのSymlink

## 使うツール・ライブラリ

- ln -s（Symlink作成）
- npx skills add（CLI installer）

## コード例

```
ln -s ../../../.github/skills/azure-ai-projects-py projects
```

## 前提知識

- AI coding agent（GitHub Copilot、Claude Code、Copilot CLI等）の基本操作
- Markdown形式のドキュメント構造理解
- Symlink（シンボリックリンク）の概念
- YAML形式の設定ファイル
- GitHub Actionsの基本（日次更新ワークフローを活用する場合）
- MCP（Model Context Protocol）の概要（外部ツール統合を使う場合）
