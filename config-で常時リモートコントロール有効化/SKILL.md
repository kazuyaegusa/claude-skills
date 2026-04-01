# /config で常時リモートコントロール有効化

> Claude Code内の `/config` コマンドで `Enable Remote Control for all sessions` を `true` に設定し、以降すべてのセッションをデフォルトでリモート接続可能にする

- 出典: https://x.com/hiragram/status/2026423131217555542
- 投稿者: hiragram/ひらり
- カテゴリ: claude-code-workflow

## なぜ使うのか

毎回 `claude rc` を入力する手間を省ける。常にリモート操作を前提とした運用スタイルの場合に省力化できる

## いつ使うのか

常にリモートから操作することが多い場合、または毎回 `claude rc` を入力するのが煩わしくなったとき

### 具体的な適用場面

- ローカルで長時間タスク（テスト・ビルド・スクレイピング等）を起動後、外出先のスマホから進捗確認・追加指示したいとき
- メインPCで作業中にタブレット・別PCからも同じセッションに接続して引き継ぎしたいとき

## やり方

1. `claude` コマンドでClaude Codeを起動する
2. チャット内で `/config` と入力して設定メニューを開く
3. `Enable Remote Control for all sessions` の項目を `true` に設定する
4. 以降は通常の `claude` 起動だけでリモート接続可能なセッションとして動作する

### 入力

- Claude Codeインストール済み環境
- Claude Code内の /config 設定メニューへのアクセス

### 出力

- 全セッションがデフォルトでリモートコントロール対応になる設定状態

## 使うツール・ライブラリ

- claude CLI（Claude Code）

## コード例

```
/config
# → Enable Remote Control for all sessions: true
```

## 前提知識

- Claude Codeがローカルマシンにインストール済みであること
- Anthropicのアカウント（Remote Control機能が有効なプラン）を持っていること
- 接続先デバイスでClaudeアプリまたはWebにアクセスできること

## 根拠

> `claude rc` で明示的にオンラインセッションにするほか

> `/config` で `Enable Remote Control for all sessions` をtrueにすることで常時ONにできる

> 自分のマシン上で開始したセッションにClaudeのWeb/デスクトップアプリ/モバイルアプリから繋いで操作できる
