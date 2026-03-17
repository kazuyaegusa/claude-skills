# AI開発ツール向けメタデータ同梱

> Claude Code・Cursor等のAIエージェントが読み取る専用ドキュメント（AGENTS.md、llms-full.txt、スキル、プラグイン）をプロジェクトに含める

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIツールは通常のREADMEだけでは「どこに何を書けばいいか」「認証の実装パターン」を理解しにくい。構造化されたメタデータを提供することで、AIが正確なコード生成を行える

## いつ使うのか

AIアシスタントにプロジェクト特有の実装パターンを学習させ、高品質なコード生成を実現したいとき

## やり方

1. プロジェクトルートに `AGENTS.md` を配置し、Waspの設定ルール・認証フロー・DB操作パターンをマークダウンで記述
2. `llms-full.txt` にプロジェクト全体のコンテキスト（ディレクトリ構造、主要API）を列挙
3. Claude Code向けに `.claude/skills/` にスキルファイルを配置
4. Cursor向けに `.cursorrules` を設置
5. AIツールで「新しい認証プロバイダを追加」等のプロンプトを投げると、メタデータを参照して正確なコードを生成

### 入力

- プロジェクトのアーキテクチャ情報
- Wasp特有の規約・ベストプラクティス

### 出力

- AIが参照可能な構造化ドキュメント
- 正確なコード生成・補完

## 使うツール・ライブラリ

- Claude Code
- Cursor
- Markdown

## コード例

```
# AGENTS.md
## Authentication
- Use `auth` block in main.wasp
- Social providers require `clientId` and `clientSecret`
- Email auth uses SendGrid/MailGun for verification
```

## 前提知識

- Node.js/npm基礎知識
- React・TypeScriptの基本構文
- Prisma ORMの概念（スキーマ定義・マイグレーション）
- REST API / HTTPクライアントの理解
- Stripe/決済APIの基本的な動作原理（サブスク課金を使う場合）
