# VibeSec-Skillで脆弱性を防ぐ

> Claude Codeでセキュアなコードを書くための専用スキル（VibeSec-Skill）を導入し、一般的な脆弱性を予防する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeはコード生成速度が速いが、セキュリティベストプラクティスを常に適用するとは限らない。セキュリティ専用スキルを使うことで、OWASP Top 10などの脆弱性を自動的にチェック・回避できる

## いつ使うのか

Claude Codeで本番環境向けのWebアプリケーションを開発する時、特にユーザー入力を処理する機能を実装する時

## やり方

1. VibeSec-Skill リポジトリをクローン
2. Claude Codeの設定にスキルを追加
3. Webアプリケーション開発時に自動的にセキュリティチェックが適用される
4. owasp-security スキルと組み合わせることで、OWASP Top 10:2025、ASVS 5.0、Agentic AI security（2026）にも対応可能

### 入力

- Claude Codeのプロジェクト
- VibeSec-SkillのGitHubリポジトリ

### 出力

- セキュリティベストプラクティスが適用されたコード
- 脆弱性の自動検出と修正提案

## 使うツール・ライブラリ

- VibeSec-Skill
- owasp-security skill（オプション）

## 前提知識

- Claude Codeの基本的な使い方（スキルのインストール・有効化方法）
- Gitの基本操作（clone, pull）
- Markdown記法の読み書き
- （スキル開発の場合）Python, Node.js, Bashのいずれかの基礎知識
- （MCP Server利用の場合）API認証（OAuth, API Key）の基本理解

## 根拠

> "A curated list of Claude Skills."

> "If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked."

> "skill-creator - Template / helper to build new Claude skills."

> "agentskill.sh - Browse and install 69,000+ AI agent skills for Claude Code, Cursor, Copilot, Windsurf, Zed, and 20+ AI tools."

> "linear-claude-skill - Manage Linear issues, projects, and teams with MCP tools"
