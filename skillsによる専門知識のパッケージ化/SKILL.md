# Skillsによる専門知識のパッケージ化

> 特定タスク（TDD、セキュリティ監査、ドキュメント生成等）に必要な知識・手順をSKILL.mdファイルとしてパッケージ化し、Claude Codeに読み込ませる

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

毎回同じ指示を与える手間を省き、ベストプラクティスを再利用可能な形で蓄積・共有できる。チーム全体で品質基準を統一できる。

## いつ使うのか

繰り返し行うタスク（コードレビュー、テスト生成、リリース作業等）がある時、チームで開発標準を共有したい時

## やり方

1. ~/.claude/skills/{skill-name}/SKILL.md を作成
2. 必要な知識・手順・制約をマークダウンで記述
3. Claude Codeセッション開始時に自動読み込み、または明示的に /skill-name で呼び出し
4. Superpowers等の既存スキルセットをベースにカスタマイズも可能

### 入力

- タスクの要件・制約・ベストプラクティス

### 出力

- SKILL.mdファイル
- Claude Codeが自動的に適用する専門知識

## 使うツール・ライブラリ

- ~/.claude/skills/ディレクトリ
- 既存スキルリポジトリ（Superpowers、AgentSys等）

## 前提知識

- Claude Codeの基本的な使い方（CLI操作、セッション管理）
- Gitの基礎知識（ブランチ、コミット、PR等）
- シェルスクリプトまたはPython/TypeScriptの基礎（Hook・Skill作成に必要）
- プロジェクトのビルド・テストコマンドの理解

## 根拠

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task

> CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards

> Alternative Clients are alternative UIs and front-ends for interacting with Claude Code, either on mobile or on the desktop.
