# 環境変数の優先度階層設計

> .envファイルを複数レベル(CLI > process.env > プロジェクト > ユーザー)で読み込み、優先度順に上書き適用する

- 出典: https://github.com/JimLiu/baoyu-skills
- 投稿者: JimLiu
- カテゴリ: claude-code-workflow

## なぜ使うのか

APIキーやエンドポイントをチーム共有(プロジェクトレベル)と個人設定(ユーザーレベル)で使い分け、かつ一時的なCLIオーバーライドも可能にすることで、柔軟かつセキュアな設定管理を実現

## いつ使うのか

複数のAPI提供者を使い分ける場合、チームと個人で異なる認証情報を使う場合

## やり方

1. ユーザーレベル: `~/.baoyu-skills/.env` を作成しAPIキー等を記載
2. プロジェクトレベル: `<cwd>/.baoyu-skills/.env` を作成(チーム共有用、gitignore推奨)
3. CLI実行時: `OPENAI_API_KEY=xxx /baoyu-imagine ...` で一時上書き
4. コード内で環境変数読み込み時、CLI > process.env > プロジェクト > ユーザー の順で上書き適用

### 入力

- .envファイル(複数レベル)
- 環境変数

### 出力

- 優先度に基づいた最終的な設定値

## 使うツール・ライブラリ

- dotenv等の環境変数ローダー

## コード例

```
# User-level config
mkdir -p ~/.baoyu-skills
cat > ~/.baoyu-skills/.env << 'EOF'
OPENAI_API_KEY=sk-xxx
EOF

# Project-level config
mkdir -p .baoyu-skills
echo '.baoyu-skills/.env' >> .gitignore
```

## 前提知識

- Claude Codeの基本的な使い方とスキルの概念
- GitHubリポジトリの作成・管理
- JSON形式の理解(plugin-marketplace.json作成のため)
- 環境変数と.envファイルの扱い方
- Bashスクリプトの基本(ClawHub公開スクリプト利用時)

## 根拠

> 「Load Priority (higher priority overrides lower): 1. CLI environment variables 2. process.env 3. <cwd>/.baoyu-skills/.env 4. ~/.baoyu-skills/.env」
