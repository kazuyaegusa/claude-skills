# Checkpointingで長時間セッションを保存・再開

> 複雑なタスク中にセッションを保存し、後で同じ状態から再開する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

長時間の開発セッションを中断・再開でき、コンテキストを失わずに作業を継続できる

## いつ使うのか

複雑なリファクタリングやマルチステップの実装で中断が必要な時

## やり方

1. セッション中に `/checkpoint save <name>` で保存
2. 後で `gemini --resume <name>` で再開
3. 保存されたチェックポイントは `~/.gemini/checkpoints/` に保存される

### 入力

- 実行中のGemini CLIセッション
- チェックポイント名

### 出力

- 保存されたセッション状態（会話履歴、コンテキスト）
- 再開可能なセッション

## 使うツール・ライブラリ

- Gemini CLI
- ~/.gemini/checkpoints/

## コード例

```
# セッション中
> /checkpoint save refactor-auth

# 再開
gemini --resume refactor-auth
```

## 前提知識

- Node.js 18以上の基本的な理解
- ターミナル操作の基礎知識
- npmパッケージマネージャーの基本的な使い方
- LLM APIの基本概念（プロンプト、トークン、コンテキストウィンドウ）
- OAuth認証フローの概要理解（ブラウザベース認証）
- JSON形式の基本的なパース方法
- （GitHub Actions利用の場合）GitHub Actionsの基本構文
- （MCP利用の場合）Model Context Protocolの概要

## 根拠

> 「Conversation checkpointing to save and resume complex sessions」（チェックポイント機能）
