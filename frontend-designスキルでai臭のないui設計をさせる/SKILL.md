# frontend-designスキルでAI臭のないUI設計をさせる

> 公式frontend-designスキルを使い、汎用的・AI特有の美学を避け、大胆なデザイン判断をClaudeに促す

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: ui-ux

## なぜ使うのか

LLMは指示なしだと無難・汎用的なデザインを生成しがちで、「AI slop」と呼ばれる特徴的な見た目になるため

## いつ使うのか

React/Tailwindでフロントエンドを実装する時、特にデザイン性を重視する場合

## やり方

1. frontend-designスキルを有効化
2. React + Tailwind CSSでのUI実装をClaudeに依頼
3. スキルが「汎用的美学を避け、大胆な判断をする」指示をClaude内部に注入

### 入力

- UI実装要件

### 出力

- 大胆なデザイン判断を含むReact+Tailwindコード

## 使うツール・ライブラリ

- frontend-design（公式スキル）
- React
- Tailwind CSS

## 前提知識

- Claude.ai Pro/Max/Team/Enterpriseアカウント（Freeユーザーはスキル利用不可）
- YAML frontmatter、Markdownの基本知識
- （API利用の場合）Anthropic APIキーとAPI仕様の理解
- （Claude Code利用の場合）Claude Code CLIのインストール

## 根拠

> frontend-design - Instructs Claude to avoid 'AI slop' or generic aesthetics and to make bold design decisions. Works very well for React & Tailwind.
