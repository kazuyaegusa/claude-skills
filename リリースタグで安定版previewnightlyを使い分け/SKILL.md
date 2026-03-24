# リリースタグで安定版・preview・nightlyを使い分け

> npmインストール時に`@latest`、`@preview`、`@nightly`タグを指定し、安定版・週次プレビュー・日次最新を選択する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: dev-tool

## なぜ使うのか

安定運用では`@latest`、新機能テストでは`@preview`、最新変更を試すなら`@nightly`と使い分けることで、リスクを管理できるため

## いつ使うのか

安定性とfeedbackサイクルをコントロールしたい場合

## やり方

1. 安定版: `npm install -g @google/gemini-cli@latest`（毎週火曜20:00 UTC）
2. プレビュー版: `npm install -g @google/gemini-cli@preview`（毎週火曜23:59 UTC）
3. Nightly版: `npm install -g @google/gemini-cli@nightly`（毎日00:00 UTC）
4. 目的に応じてタグを選択してインストール

### 入力

- npmインストールコマンド
- リリースタグ（latest, preview, nightly）

### 出力

- 指定バージョンのGemini CLI

## 使うツール・ライブラリ

- npm
- @google/gemini-cli

## コード例

```
npm install -g @google/gemini-cli@preview
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Googleアカウント（OAuth認証用）
- ターミナル操作の基礎知識
- （GitHub連携時）GitHubリポジトリとActions実行権限
- （MCP統合時）各サービスのAPI認証情報
