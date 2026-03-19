# セキュリティスキル（VibeSec, OWASP, Trail of Bits）を導入して脆弱性を予防する

> Security & Web Testing カテゴリのスキル（VibeSec-Skill, owasp-security, Trail of Bits Security Skills）をClaude Codeに追加し、コード生成時に自動的にセキュリティベストプラクティスを適用させる

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeが生成するコードはデフォルトでセキュリティを完全に考慮しないため、スキルとして脆弱性チェックリスト・OWASP Top 10・静的解析ルールを組み込むことで、XSS/SQLi/認証欠陥等を事前に防止できる

## いつ使うのか

Webアプリ、API、認証機能など、セキュリティリスクの高いコードをClaude Codeで生成する時

## やり方

1. VibeSec-Skill, owasp-security, Trail of Bits Security Skills のいずれかをGitHubからクローン
2. SKILL.md を `~/.claude/skills/` に配置
3. Claude Codeに「Webアプリを書いて」と依頼する際、自動的にスキルが適用され、セキュアなコードパターンが使われる
4. コードレビュー時にスキルのチェックリスト（OWASP ASVS 5.0等）を参照して検証

### 入力

- セキュリティ要件（例: OWASP Top 10準拠、PII保護、SQL injection対策）

### 出力

- 脆弱性が低減されたコード
- セキュリティチェックリストに基づくレビュー結果

## 使うツール・ライブラリ

- VibeSec-Skill
- owasp-security (OWASP Top 10:2025, ASVS 5.0)
- Trail of Bits Security Skills (CodeQL, Semgrep)

## 前提知識

- Claude Codeの基本的な使い方（スキルの配置場所 ~/.claude/skills/ の理解）
- GitHubリポジトリのクローン方法
- npm/npx の基本操作（一部スキルのインストールに必要）
- MCP（Model Context Protocol）の概念（外部ツール連携スキルを使う場合）

## 根拠

> 投稿タイトル: 'BehiSecc/awesome-claude-skills - A curated list of Claude Skills.'

> カテゴリ分類: '📄 Document Skills', '🛠 Development & Code Tools', '📊 Data & Analysis', '🔬 Scientific & Research Tools', '✍️ Writing & Research', '📘 Learning & Knowledge', '🎬 Media & Content', '🏥 Health & Life Sciences', '🤝 Collaboration & Project Management', '🛡 Security & Web Testing', '🔧 Utility & Automation', '🗂️ Collections'

> 収録スキル例: 'docx - Create, edit, analyze Word docs with tracked changes', 'test-driven-development - Use when implementing any feature or bugfix', 'VibeSec-Skill - VibeSec helps Claude write secure code and prevent common vulnerabilities', 'pm-skills - 24 product management skills across the Triple Diamond lifecycle'

> コレクション例: 'OpenPaw - 38-skill bundle that turns Claude Code into a personal assistant. Run via npx pawmode', 'agentskill.sh - Browse and install 69,000+ AI agent skills'

> Tip: 'If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked.'
