# ClawHub個別スキル公開スクリプト

> `scripts/sync-clawhub.sh` を使い、`skills/baoyu-*` 各ディレクトリをClawHubレジストリに個別スキルとして公開する

- 出典: https://github.com/JimLiu/baoyu-skills
- 投稿者: JimLiu
- カテゴリ: claude-code-workflow

## なぜ使うのか

ClawHubはスキル単位でのインストールを前提としており、Marketplace的な一括登録をサポートしない。個別公開により `clawhub install baoyu-imagine` のようなスキル単位インストールが可能になる

## いつ使うのか

ClawHubエコシステムのユーザーにもスキルを提供したい場合。スキルごとの個別インストールをサポートしたい場合

## やり方

1. `./scripts/sync-clawhub.sh --dry-run` で公開対象を確認
2. `./scripts/sync-clawhub.sh --all` で全変更スキルをClawHubに公開
3. ClawHubはMIT-0ライセンスでスキルを登録
4. ユーザーは `clawhub install baoyu-imagine` で個別インストール可能

### 入力

- skills/ディレクトリ配下の各スキル
- ClawHub CLI

### 出力

- ClawHubレジストリへの個別スキル公開
- スキル単位でのインストール対応

## 使うツール・ライブラリ

- ClawHub CLI
- Bashスクリプト

## コード例

```
# Preview what would be published
./scripts/sync-clawhub.sh --dry-run

# Publish all changed skills from ./skills
./scripts/sync-clawhub.sh --all
```

## 前提知識

- Claude Codeの基本的な使い方とスキルの概念
- GitHubリポジトリの作成・管理
- JSON形式の理解(plugin-marketplace.json作成のため)
- 環境変数と.envファイルの扱い方
- Bashスクリプトの基本(ClawHub公開スクリプト利用時)
