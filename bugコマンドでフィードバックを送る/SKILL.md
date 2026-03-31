# /bugコマンドでフィードバックを送る

> Claude Code内で `/bug` コマンドを実行し、問題報告を直接送信する

- 出典: https://github.com/anthropics/claude-code
- 投稿者: anthropics
- カテゴリ: claude-code-workflow

## なぜ使うのか

バグや改善要望を開発チームに迅速に伝えることで、ツールの品質向上に貢献でき、自分の環境での問題解決も早まる

## いつ使うのか

Claude Code使用中にバグや不具合を発見した時、機能要望がある時

## やり方

1. Claude Codeセッション内で `/bug` と入力
2. 問題の詳細を記述
3. 送信（または[GitHub issue](https://github.com/anthropics/claude-code/issues)を直接作成）

### 入力

- 問題の説明文
- 再現手順（任意）

### 出力

- フィードバック送信完了通知
- 開発チームへのレポート

## 使うツール・ライブラリ

- Claude Code内蔵コマンド

## コード例

```
# Claude Codeセッション内で
/bug
```

## 前提知識

- ターミナル操作の基本知識
- Gitの基本的な概念（コミット、PR）
- Node.js環境（npm経由インストール時）
- Anthropic APIキーまたはClaude Codeサブスクリプション
- コーディング経験（対象コードベースの言語に対する基本理解）

## 根拠

> "Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows -- all through natural language commands."

> "curl -fsSL https://claude.ai/install.sh | bash"

> "This repository includes several Claude Code plugins that extend functionality with custom commands and agents."

> "Use the `/bug` command to report issues directly within Claude Code"

> "Learn more in the [official documentation](https://code.claude.com/docs/en/overview)."
