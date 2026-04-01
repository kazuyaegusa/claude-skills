# npx skills add によるクイックインストール

> `npx skills add jimliu/baoyu-skills` コマンドで、npm経由でスキルを直接インストールする

- 出典: https://github.com/JimLiu/baoyu-skills
- 投稿者: JimLiu
- カテゴリ: claude-code-workflow

## なぜ使うのか

Marketplace登録やClawHubセットアップ不要で、GitHub URLさえあればワンコマンドでインストールできる。新規ユーザーの導入障壁を最小化

## いつ使うのか

初回インストール時、またはMarketplace未登録の段階で素早くスキルを試したい場合

## やり方

1. ユーザーがターミナルで `npx skills add jimliu/baoyu-skills` を実行
2. npxがGitHubリポジトリからスキルをcloneまたはダウンロード
3. スキルが自動的にClaude Codeのスキルディレクトリに配置される

### 入力

- GitHubリポジトリパス(jimliu/baoyu-skills)

### 出力

- Claude Codeへのスキルインストール

## 使うツール・ライブラリ

- npx
- skills CLI

## コード例

```
npx skills add jimliu/baoyu-skills
```

## 前提知識

- Claude Codeの基本的な使い方とスキルの概念
- GitHubリポジトリの作成・管理
- JSON形式の理解(plugin-marketplace.json作成のため)
- 環境変数と.envファイルの扱い方
- Bashスクリプトの基本(ClawHub公開スクリプト利用時)

## 根拠

> 「npx skills add jimliu/baoyu-skills」でクイックインストール可能

> 「/plugin marketplace add JimLiu/baoyu-skills」でMarketplace登録

> 「Load Priority (higher priority overrides lower): 1. CLI environment variables 2. process.env 3. <cwd>/.baoyu-skills/.env 4. ~/.baoyu-skills/.env」

> 「Extension paths (checked in priority order): 1. .baoyu-skills/<skill-name>/EXTEND.md 2. ~/.baoyu-skills/<skill-name>/EXTEND.md」
