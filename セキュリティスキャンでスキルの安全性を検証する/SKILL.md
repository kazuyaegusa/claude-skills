# セキュリティスキャンでスキルの安全性を検証する

> スキルをインストール前にSKILL.mdと全スクリプトをレビューし、悪意あるコード・プロンプトインジェクション・データ流出リスクを確認する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

Skillsは任意のコードを実行できるため、信頼できないソースからのスキルはセキュリティリスクとなる

## いつ使うのか

信頼できないソースからスキルをインストールする前、エンタープライズ環境で導入する前

## やり方

1. SKILL.mdと全スクリプトを読む
2. センシティブデータへのアクセス要求がないか確認
3. 外部API呼び出し・ネットワーク通信の妥当性を確認
4. プロンプトインジェクション攻撃の可能性を検討
5. 本番/エンタープライズ環境導入前に非本番環境でテスト
6. 参考: 'Weaponizing Claude Code Skills' セキュリティ研究

### 入力

- インストール対象のスキルディレクトリ

### 出力

- セキュリティリスク評価
- 導入可否判断

## 使うツール・ライブラリ

- コードレビュー
- セキュリティ監査

## 前提知識

- Claude.ai Pro/Max/Team/Enterpriseアカウント（Freeユーザーはスキル利用不可）
- YAML frontmatter、Markdownの基本知識
- （API利用の場合）Anthropic APIキーとAPI仕様の理解
- （Claude Code利用の場合）Claude Code CLIのインストール

## 根拠

> Use Skills when: Capabilities should be accessible to any Claude instance. They're portable expertise.

> ⚠️ Important: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.

> frontend-design - Instructs Claude to avoid 'AI slop' or generic aesthetics and to make bold design decisions. Works very well for React & Tailwind.

> obra/superpowers - Core skills library for Claude Code with 20+ battle-tested skills including TDD, debugging, and collaboration patterns
