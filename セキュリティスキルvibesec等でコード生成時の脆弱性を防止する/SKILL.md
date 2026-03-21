# セキュリティスキル（VibeSec等）でコード生成時の脆弱性を防止する

> VibeSec-SkillなどのセキュリティスキルをClaude Codeに統合し、生成されるコードが一般的な脆弱性（OWASP Top 10等）を含まないようにする

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

LLMが生成するコードはSQLインジェクション、XSS、認証バイパス等の脆弱性を含む可能性がある。セキュリティスキルを事前ロードすることで、生成段階から安全なコードを出力できる

## いつ使うのか

Webアプリケーション、API、認証システム等、セキュリティが重要なコードをClaude Codeで生成する際は必須

## やり方

1. VibeSec-Skill（https://github.com/BehiSecc/VibeSec-Skill）をクローン
2. SKILL.mdを`~/.claude/skills/vibesec/`に配置
3. Claude Codeを起動し、Webアプリ開発タスクを実行
4. Claude Codeは自動的にOWASP Top 10、入力検証、認証・認可のベストプラクティスを適用したコードを生成
5. （オプション）owasp-securityスキルと組み合わせてASVS 5.0準拠の徹底的なレビューを実施

### 入力

- セキュリティスキル（VibeSec, owasp-security等）
- 開発対象のコード・アプリケーション

### 出力

- OWASP Top 10対策済みのコード
- セキュリティレビュー結果

## 使うツール・ライブラリ

- VibeSec-Skill
- owasp-security
- Claude Code

## 前提知識

- Claude Codeの基本的な使い方（スキルのロード・呼び出し方法）
- GitHubの基本操作（リポジトリのクローン、ファイル取得）
- Markdownの読み書き
- ~/.claude/skills/ディレクトリの存在と役割の理解

## 根拠

> 「A curated list of Claude Skills.」

> 「If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked.」（セキュリティの重要性を強調）

> 「skill-creator - Template / helper to build new Claude skills.」（公式テンプレート存在）

> 「OpenPaw - 38-skill bundle that turns Claude Code into a personal assistant.」（コレクション例）

> 「agentskill.sh - Browse and install 69,000+ AI agent skills for Claude Code, Cursor, Copilot, Windsurf, Zed, and 20+ AI tools.」（エコシステムの規模）
