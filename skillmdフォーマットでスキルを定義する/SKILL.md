# SKILL.mdフォーマットでスキルを定義する

> Claude Codeが読み込める標準フォーマット（SKILL.md）でスキルの動作・トリガー条件・ツール呼び出しを記述する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

スキルをマークダウンで宣言的に定義することで、コード不要でAIの動作をカスタマイズでき、非プログラマーでもスキルを作成・共有できる

## いつ使うのか

特定のワークフロー（TDD、セキュリティレビュー、git操作等）をClaude Codeに標準装備させたい時、チーム全体で同じAI支援を受けたい時

## やり方

1. リポジトリルートまたは`~/.claude/skills/`配下に`SKILL.md`を作成
2. frontmatterで`name`と`description`を定義（スキルの自動起動条件）
3. 本文にスキルの目的、使用タイミング、具体的な手順（チェックリスト形式）を記述
4. 必要に応じてツール呼び出し例やコードスニペットを含める
5. Claude Codeセッション開始時、条件に合致すればスキルが自動ロードされる

### 入力

- スキルのトリガー条件（description）
- 実行する手順やチェックリスト
- （オプション）ツール名やAPIエンドポイント

### 出力

- Claude Codeが自動認識する`SKILL.md`ファイル
- 条件に応じて起動するカスタムAI動作

## 使うツール・ライブラリ

- Claude Code
- Markdown

## コード例

```
---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

## Workflow
1. Write failing test first
2. Implement minimal code to pass
3. Refactor while keeping tests green
```

## 前提知識

- Claude Codeの基本的な使い方（プロンプト実行、ツール呼び出し）
- GitHubリポジトリのクローン・PRの基本操作
- SKILL.mdの配置場所（`~/.claude/skills/`）の理解
- （MCPスキル使用時）Model Context Protocolの概念とサーバーインストール方法

## 根拠

> 「A curated list of Claude Skills」

> 「100以上のスキルリンク（docx, pdf, test-driven-development, VibeSec-Skill, aws-skills, postgres, linear-claude-skill等）」

> 「[Tip] If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked」
