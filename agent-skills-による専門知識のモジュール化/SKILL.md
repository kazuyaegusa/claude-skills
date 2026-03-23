# Agent Skills による専門知識のモジュール化

> 特定ドメイン（セキュリティ監査、科学計算、デザインレビューなど）の専門知識をスキルファイルとしてパッケージ化し、Claude Code に追加する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude の汎用知識だけでは不足する専門的なタスク（脆弱性検出、数値計算、UI/UX 評価など）を、専門家が作成したスキルで補強できるため

## いつ使うのか

セキュリティ監査を自動化したい時、科学論文執筆を支援したい時、UI/UX レビューを体系的に行いたい時

## やり方

1. `~/.claude/skills/` ディレクトリにスキルファイル（Markdown）を配置
2. スキルファイルにドメイン知識、チェックリスト、コマンド例を記述
3. Claude Code セッション中にスキルを明示的に呼び出す、または自動検出させる
4. スキルの指示に従って Claude がタスクを実行

### 入力

- スキルファイル（Markdown 形式）
- ドメイン固有の知識・チェックリスト

### 出力

- 専門的なタスクの実行結果
- レポート・推奨事項

## 使うツール・ライブラリ

- Trail of Bits Security Skills（脆弱性検出）
- Claude Scientific Skills（研究・科学計算）
- Design Review Workflow（UI/UX 評価）

## コード例

```
---
name: security-audit
description: Perform security audit using CodeQL
---

1. Run CodeQL analysis
2. Check for SQL injection, XSS, CSRF
3. Validate input sanitization
4. Review authentication/authorization logic
```

## 前提知識

- Claude Code の基本的な使い方（インストール、セッション開始、プロンプト入力）
- Git の基礎知識（コミット、ブランチ、PR 作成）
- Markdown の基本文法
- シェルスクリプト（Bash）の基礎知識（フック・スラッシュコマンドのカスタマイズに必要）
- JSON の基本構造（フック設定ファイルの編集に必要）

## 根拠

> "A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow."

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"
