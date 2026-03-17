# frontend-design Skillで「AIっぽいデザイン」を回避する

> frontend-design Skillを使い、Claude生成のReact+Tailwindコードで平凡な美学を避け、大胆なデザイン決定を促す

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: ui-ux

## なぜ使うのか

デフォルトではClaude生成UIが「AIスロップ」（無難で個性のないデザイン）になりがち。Skillで明示的に美学を指示することで、ユニークで魅力的なUIを得られる。

## いつ使うのか

React+Tailwindでフロントエンド開発中、視覚的に魅力的なUIを短時間で作りたい時

## やり方

1. frontend-design Skillを有効化 2. React+Tailwindコンポーネント生成を依頼 3. Skillが自動的に「大胆なデザイン決定」「AI臭さを避ける」指示を適用 4. 生成されたコードを確認・調整

### 入力

- UIコンポーネントの要件

### 出力

- React+Tailwindコード（個性的なデザイン適用済み）

## 使うツール・ライブラリ

- frontend-design Skill
- React
- Tailwind CSS

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（SkillsはFree tierでは利用不可）
- YAML基礎知識（フロントマター記述用）
- gitとバージョン管理の基本（Skillsの配布・管理用）
- Python/JavaScriptの基礎（スクリプト含むSkill作成時）
- Claude.ai / Claude Code CLI / Claude APIのいずれかの利用経験

## 根拠

> frontend-design - Instructs Claude to avoid 'AI slop' or generic aesthetics and to make bold design decisions. Works very well for React & Tailwind.
