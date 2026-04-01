# AI対応設定の同梱（AGENTS.md/Skills）

> プロジェクト生成時にAGENTS.md、Claude Code Skills、プラグインが自動配置され、AI支援開発が即座に可能

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: claude-code-workflow

## なぜ使うのか

通常AIツールはプロジェクト構造・使用フレームワークを学習する必要があるが、Open SaaSは事前設定済みのルール・スキルを提供することで初回から高精度な支援を得られるため

## いつ使うのか

Claude Code/Cursor等のAI支援開発ツールで効率的にSaaSを構築したい時

## やり方

1. `wasp new -t saas` でプロジェクト生成
2. AGENTS.md、.claude/skills/、プラグイン設定が自動配置される
3. Claude Code/Cursor等で開くだけで、Wasp固有の開発パターンをAIが理解
4. 認証追加・API作成等をAIに依頼可能

### 入力

- Open SaaSテンプレート生成コマンド

### 出力

- AI向けプロジェクトドキュメント（AGENTS.md）
- フレームワーク固有Skills
- Claude Codeプラグイン設定

## 使うツール・ライブラリ

- Claude Code
- Cursor
- その他AIコーディングツール

## 前提知識

- Node.js基礎知識（npm/yarn操作）
- React基礎（コンポーネント、Hooks）
- TypeScript基礎（型アノテーション）
- Prisma ORM基本概念（スキーマ定義、マイグレーション）
- SaaS基本概念（認証、決済フロー、サブスクリプション）

## 根拠

> 「Full-stack Authentication - Email verified + social Auth in a few lines of code」

> 「AI-Ready - Custom Plugins, Skills, & Rules for AI-assisted coding with Claude Code, Cursor, or your favorite AI-assisted coding tool」

> コマンド例: `npm i -g @wasp.sh/wasp-cli` → `wasp new -t saas`
