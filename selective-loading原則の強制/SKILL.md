# Selective loading原則の強制

> README.mdで「Use skills selectively. Loading all skills causes context rot」と明示し、必要なスキルのみをコピー/Symlinkする運用を推奨する

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

全スキルをロードすると注意が分散し、トークンを浪費し、パターンが混同される（context rot）

## いつ使うのか

新規プロジェクトでスキルカタログを導入する際、または既存プロジェクトでスキルを整理する際

## やり方

1. プロジェクト開始時に必要なスキルを特定 2. `npx skills add microsoft/skills` で対話的に選択、または `cp -r .github/skills/<skill> your-project/.github/skills/` で個別コピー 3. 不要なスキルは削除

### 入力

- プロジェクトの技術スタック
- 使用するAzure/Foundryサービス

### 出力

- プロジェクト固有の `.github/skills/` ディレクトリ（5-15スキル程度）

## 使うツール・ライブラリ

- npx skills add
- cp/ln -s

## コード例

```
# 悪い例: 全スキルをコピー
cp -r agent-skills/.github/skills/* .
# 良い例: 必要なもののみ
cp -r agent-skills/.github/skills/azure-cosmos-db-py .
```

## 前提知識

- AI coding agent（GitHub Copilot、Claude Code、Copilot CLI等）の基本操作
- Markdown形式のドキュメント構造理解
- Symlink（シンボリックリンク）の概念
- YAML形式の設定ファイル
- GitHub Actionsの基本（日次更新ワークフローを活用する場合）
- MCP（Model Context Protocol）の概要（外部ツール統合を使う場合）

## 根拠

> 「Use skills selectively. Loading all skills causes context rot: diluted attention, wasted tokens, conflated patterns.」（README.md）

> 「The patterns are already in their weights from pretraining. All you need is the right activation context to surface them.」（README.md）

> 「132 skills in `.github/skills/` — flat structure with language suffixes for automatic discovery」（Skill Catalog）

> 「Ralph Loop — An iterative code generation and improvement system that: 1. Generate code 2. Evaluate against acceptance criteria 3. Analyze failures 4. Re-generate with feedback 5. Report on quality improvements」（Testing Skills）

> 「Skills are installed to your chosen agent's directory (e.g., `.github/skills/` for GitHub Copilot) and symlinked if you use multiple agents.」（Quick Start）
