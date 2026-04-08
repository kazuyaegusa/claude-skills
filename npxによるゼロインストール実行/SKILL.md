# npxによるゼロインストール実行

> npmグローバルインストール不要で、npx経由で即座にGemini CLIを起動する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

環境汚染を避け、試用ハードルを下げ、バージョン固定実行を容易にするため

## いつ使うのか

初回試用時、複数バージョン併用時、CI環境での一時実行時

## やり方

1. `npx @google/gemini-cli` を実行
2. 初回実行時はOAuth認証フローが起動
3. ブラウザでGoogle認証完了後、ターミナルで対話開始

### 入力

- Google アカウント（OAuth認証用）

### 出力

- 対話型AIセッション開始

## 使うツール・ライブラリ

- npx
- @google/gemini-cli

## コード例

```
npx @google/gemini-cli
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Google アカウント（OAuth認証用）
- （任意）Gemini API Key または Vertex AI認証情報
- （GitHub Action利用時）GitHub リポジトリ管理権限
- （MCP利用時）各MCPサーバーのセットアップ知識
