# リリースチャンネル（nightly/preview/stable）の使い分け

> npm タグを指定して、nightly/preview/stable版を選択的にインストール・テストする

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

最新機能の先行利用、安定版での本番利用を切り替えるため

## いつ使うのか

新機能テスト時はnightly、本番環境はstable、早期採用者はpreview

## やり方

1. `npm install -g @google/gemini-cli@nightly` で最新開発版を取得
2. `@preview` で週次ベータ版、`@latest` で安定版を指定
3. 環境ごとに異なるバージョンを使い分け

### 入力

- npm タグ指定

### 出力

- 指定バージョンのGemini CLI

## 使うツール・ライブラリ

- npm

## コード例

```
npm install -g @google/gemini-cli@nightly   # 最新開発版
npm install -g @google/gemini-cli@preview   # 週次ベータ版
npm install -g @google/gemini-cli@latest    # 安定版
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Google アカウント（OAuth認証用）
- （任意）Gemini API Key または Vertex AI認証情報
- （GitHub Action利用時）GitHub リポジトリ管理権限
- （MCP利用時）各MCPサーバーのセットアップ知識
