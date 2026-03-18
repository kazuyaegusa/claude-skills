# Instructionsによるファイルパターン別コーディング規約の自動適用

> 特定のファイルパターン（例: *.ts, *.py）に対して自動適用されるコーディング規約やスタイルガイドをInstructionsとして定義・配布する

- 出典: https://github.com/github/awesome-copilot
- 投稿者: github
- カテゴリ: prompt-engineering

## なぜ使うのか

手動でプロンプトに規約を書く手間を省き、プロジェクト全体で一貫したコード生成を保証する

## いつ使うのか

チーム全体で統一されたコーディングスタイル、命名規則、エラーハンドリングパターンを強制したい時

## やり方

1. Awesome Copilot Webサイトまたはリポジトリの `docs/README.instructions.md` から適用したいInstructionを探す
2. Instructionファイル（.mdファイル）をプロジェクトまたはグローバル設定に配置
3. ファイルパターンに応じてCopilotが自動的にInstructionを読み込み、コード生成時に適用
4. 独自Instructionを作成する場合はCONTRIBUTING.mdを参照してリポジトリにPR

### 入力

- ファイルパターン（例: **/*.ts, **/*.py）
- コーディング規約を記述したMarkdownファイル

### 出力

- 指定パターンのファイル編集時にCopilotが規約に沿ったコードを生成
- 一貫性のあるコードベース

## 使うツール・ライブラリ

- GitHub Copilot
- VS Code
- Awesome Copilot Instructions collection

## 前提知識

- GitHub Copilot（個人またはOrganizationサブスクリプション）
- VS CodeまたはCopilot CLI
- 基本的なGit操作知識
- 対象技術スタック（導入するagents/skills/instructionsが対象とする言語・フレームワーク）の基礎知識

## 根拠

> 「A community-created collection of custom agents, instructions, skills, hooks, workflows, and plugins to supercharge your GitHub Copilot experience.」

> 「copilot plugin install <plugin-name>@awesome-copilot」

> 「Agents: Specialized Copilot agents that integrate with MCP servers」

> 「Hooks: Automated actions triggered during Copilot agent sessions」
