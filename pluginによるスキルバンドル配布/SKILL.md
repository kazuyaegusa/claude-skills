# Pluginによるスキルバンドル配布

> 関連スキル・エージェント・コマンドを `.github/plugins/<plugin-name>/` にまとめ、`npx skills add` または `/plugin install` で一括インストール可能にする

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

個別にスキルをコピーする手間を省き、テーマ別（Azure SDK、AI、Wiki生成等）にキュレーションされたスキルセットを配布する

## いつ使うのか

特定ドメイン（Azure、M365、Deep Wiki等）向けにスキルをパッケージ化して配布したい場合。社内カタログを構築する場合

## やり方

1. `.github/plugins/<plugin-name>/skills/` にスキルを配置 2. `plugin.json` で metadata を定義 3. `npx skills add microsoft/skills` で wizard起動、または `/plugin marketplace add microsoft/skills` → `/plugin install <plugin-name>@skills` で導入

### 入力

- スキル群
- plugin.json（name, description, commands等）

### 出力

- ユーザーの `.github/skills/` または `.claude/skills/` にインストール済みスキル

## 使うツール・ライブラリ

- npx skills
- Copilot CLI /plugin コマンド

## コード例

```
/plugin marketplace add microsoft/skills
/plugin install deep-wiki@skills
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

> 「132 skills in `.github/skills/` — flat structure with language suffixes for automatic discovery」（Skill Catalog）

> 「Ralph Loop — An iterative code generation and improvement system that: 1. Generate code 2. Evaluate against acceptance criteria 3. Analyze failures 4. Re-generate with feedback 5. Report on quality improvements」（Testing Skills）

> 「Skills are installed to your chosen agent's directory (e.g., `.github/skills/` for GitHub Copilot) and symlinked if you use multiple agents.」（Quick Start）

> 「Create acceptance criteria in `.github/skills/<skill>/references/acceptance-criteria.md` — Document correct/incorrect import patterns, authentication patterns, async variants」（Contributing）
