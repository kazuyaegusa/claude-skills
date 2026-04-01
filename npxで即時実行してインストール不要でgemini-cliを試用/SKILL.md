# npxで即時実行してインストール不要でGemini CLIを試用

> npmパッケージをローカルインストールせず、npxコマンドで一時的にGemini CLIを起動する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

グローバルインストールやパッケージマネージャー設定なしに、動作確認や一時利用が可能。インストール失敗リスクを回避し、試用のハードルを下げる

## いつ使うのか

初めてGemini CLIを試す時、CI環境で一時的に実行する時、複数バージョンを切り替えたい時

## やり方

1. `npx @google/gemini-cli` を実行
2. 初回起動時に認証フロー（OAuth or APIキー）を選択
3. プロンプトを入力して動作確認
4. 不要ならそのまま終了（パッケージキャッシュは自動管理される）

### 入力

- Node.js 18以上がインストール済み
- ネットワーク接続（npmレジストリへのアクセス）

### 出力

- Gemini CLIの対話セッション起動
- プロンプトへの応答

## 使うツール・ライブラリ

- npx (npm 5.2.0+に同梱)
- @google/gemini-cli

## コード例

```
npx @google/gemini-cli
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
