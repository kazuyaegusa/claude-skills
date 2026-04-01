# Wasp CLIでSaaSテンプレート初期化

> Open SaaSテンプレート一式（認証・決済・UI・AI設定含む）を新規ディレクトリに展開する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動で各サービスを統合すると数週間かかる作業を数分に短縮し、実装ミス・設定漏れを防ぐため

## いつ使うのか

SaaSプロジェクト新規作成時、または既存プロジェクトのリファレンス実装が必要な時

## やり方

1. `npm i -g @wasp.sh/wasp-cli` でWasp CLIをグローバルインストール
2. `wasp new -t saas` で新規プロジェクトを作成（`-t saas`がOpen SaaSテンプレート指定）
3. 生成されたディレクトリに移動してプロジェクト開発開始

### 入力

- Node.js環境（macOS/Linux/Windows WSL）
- npm/yarn

### 出力

- React + NodeJS + Prismaプロジェクト一式
- 認証フロー実装済み（Email/Google/GitHub/Slack/MS）
- Stripe/Polar.sh決済統合コード
- ShadCN UIコンポーネント
- AGENTS.md、Skills、Claude Codeプラグイン

## 使うツール・ライブラリ

- Wasp CLI
- npm

## コード例

```
npm i -g @wasp.sh/wasp-cli
wasp new -t saas
```

## 前提知識

- Node.js基礎知識（npm/yarn操作）
- React基礎（コンポーネント、Hooks）
- TypeScript基礎（型アノテーション）
- Prisma ORM基本概念（スキーマ定義、マイグレーション）
- SaaS基本概念（認証、決済フロー、サブスクリプション）

## 根拠

> コマンド例: `npm i -g @wasp.sh/wasp-cli` → `wasp new -t saas`
