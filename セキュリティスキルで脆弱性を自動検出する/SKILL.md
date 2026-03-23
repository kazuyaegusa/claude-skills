# セキュリティスキルで脆弱性を自動検出する

> OWASP Top 10、ASVS、Agentic AI Securityの知識をSKILL.mdに埋め込み、Claude Codeにコードレビュー・脆弱性検出を実行させる

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

AI生成コードはSQLインジェクション、XSS、認証バイパス等の脆弱性を含みやすい。セキュリティスキルを常時有効化することで、コード生成時にリアルタイムで問題を検出・修正できる

## いつ使うのか

Webアプリ開発時、Claude Codeで生成したコードを本番投入する前に安全性を担保したい時、セキュリティレビュワーがいないチームでの開発時

## やり方

1. VibeSec-SkillやOWASP-securityスキルをインストール
2. スキルはコード生成前後に自動起動し、OWASP Top 10チェックリストを適用
3. 脆弱性が見つかれば、具体的なコード例と修正案を提示
4. 言語固有の落とし穴（PHPのtype juggling、Pythonのpickle等）もカバー

### 入力

- 生成されたコード
- 対象言語（20以上の言語に対応）

### 出力

- OWASP準拠のセキュリティレビュー結果
- 脆弱性の修正コード例

## 使うツール・ライブラリ

- VibeSec-Skill
- owasp-security
- Trail of Bits Security Skills

## コード例

```
# VibeSec-Skill auto-activates on web app code generation
# Checks: SQL injection, XSS, CSRF, auth bypass, etc.
# Output: Secure code patterns + language-specific quirks
```

## 前提知識

- Claude Codeの基本的な使い方（プロンプト実行、ツール呼び出し）
- GitHubリポジトリのクローン・PRの基本操作
- SKILL.mdの配置場所（`~/.claude/skills/`）の理解
- （MCPスキル使用時）Model Context Protocolの概念とサーバーインストール方法
