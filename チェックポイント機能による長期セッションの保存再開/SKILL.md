# チェックポイント機能による長期セッションの保存・再開

> 対話セッションを途中保存し、後から同じ文脈で再開する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

複雑なタスクを複数日にわたって進める際、文脈を失わないため

## いつ使うのか

長期リファクタリング、大規模設計議論、段階的実装時

## やり方

1. セッション中に `/checkpoint` コマンド実行
2. チェックポイントファイルが保存される
3. 次回起動時に `gemini --resume <checkpoint-file>` で再開

### 入力

- /checkpoint コマンド

### 出力

- チェックポイントファイル

## 使うツール・ライブラリ

- Gemini CLI

## コード例

```
# セッション中
> /checkpoint

# 次回再開
gemini --resume ~/.gemini/checkpoints/session-20230415.json
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Google アカウント（OAuth認証用）
- （任意）Gemini API Key または Vertex AI認証情報
- （GitHub Action利用時）GitHub リポジトリ管理権限
- （MCP利用時）各MCPサーバーのセットアップ知識
