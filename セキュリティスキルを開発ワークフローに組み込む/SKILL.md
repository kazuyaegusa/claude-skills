# セキュリティスキルを開発ワークフローに組み込む

> VibeSec-Skill（OWASP Top 10対応）やTrail of Bits Skills（CodeQL/Semgrep）をClaude Codeに導入し、コード生成時に自動的にセキュリティチェックを実施する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

LLMが生成するコードは脆弱性を含む可能性が高い（SQLインジェクション、XSS等）。開発初期からセキュリティスキルを適用することで、後工程でのペネトレーションテストや修正コストを削減できる

## いつ使うのか

Webアプリケーション開発でユーザー入力を扱う時、API認証・認可を実装する時、LLMに初めてコードを生成させる時

## やり方

1. ~/.claude/skills/ に VibeSec-Skill をクローン
2. SKILL.md にOWASP Top 10:2025、ASVS 5.0のチェックリストを記載
3. Claude Codeでコード生成時、自動的にセキュリティパターンをレビュー
4. Trail of Bits Skills でCodeQL/Semgrepによる静的解析を実行
5. 脆弱性が見つかった場合、修正案を提示

### 入力

- 生成されたコード（Python, JavaScript, Go等）
- OWASP Top 10チェックリスト

### 出力

- 脆弱性レポート
- 修正済みコード

## 使うツール・ライブラリ

- VibeSec-Skill
- Trail of Bits Skills
- CodeQL
- Semgrep

## 前提知識

- Claude Codeの基本的な使い方（スキルのインストール・実行）
- GitHubでのリポジトリ検索・クローン操作
- ~/.claude/skills/ ディレクトリ構造の理解
- （オプション）MCP（Model Context Protocol）の概念

## 根拠

> "A curated list of Claude Skills."

> "If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked."

> "[claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) - 125+ scientific skills for bioinformatics, cheminformatics, clinical research, and machine learning."

> "[web-artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) - Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui)."

> "[VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) - VibeSec helps Claude write secure code and prevent common vulnerabilities."
