# HappyでClaude Code/Codexをモバイル対応させる

> ローカルPCで `happy` CLIを起動し、iOS/Android/Webアプリからそのセッションに接続してClaude Code/Codexを操作する

- 出典: https://x.com/gaijineers/status/2021043018498015248
- 投稿者: gaijineers
- カテゴリ: claude-code-workflow

## なぜ使うのか

デスクトップ以外のデバイスからも同じAI開発セッションにアクセスでき、場所やデバイスに縛られず作業を継続できるため

## いつ使うのか

移動中・外出先からClaude Codeセッションを操作したい、または複数デバイスで同じセッションを共有したいとき

### 具体的な適用場面

- 通勤中にスマホでClaude Codeセッションをレビュー・指示を追加したい
- 自宅PCで開始したCodexセッションを外出先のタブレットから継続したい
- チームで同じClaude Codeセッションを共有・引き継ぎたい
- デスクトップ環境がないときにブラウザだけでAIコーディングを行いたい

## やり方

1. PCで `npm install -g happy-coder` を実行してCLIをインストール
2. `happy` コマンド（Claude Code相当）または `happy codex` コマンド（Codex相当）を実行してサーバーを起動
3. iOS App Store / Google Play / https://app.happy.engineering からHappyクライアントをダウンロード
4. アプリでQRコードスキャンまたはペアリングコードを入力してPCと接続
5. アプリからプロンプトを送信すると、PC上のClaude/Codexが実行され、結果が暗号化通信でアプリに返される

### 入力

- Claude Code または Codex がインストール済みのPC
- Node.js (npm) 実行環境
- iOS/Android/Webブラウザのいずれか

### 出力

- モバイル/Webからアクセス可能なClaude Code/Codexセッション
- E2E暗号化されたリモート操作環境

## 使うツール・ライブラリ

- happy-coder CLI (npm package)
- Happy iOS app
- Happy Android app
- happy.engineering Web app

## コード例

```
# インストール
npm install -g happy-coder

# Claude Code相当を起動
happy

# Codex相当を起動
happy codex
```

## 前提知識

- Claude Code または Codex が既にインストールされている
- Node.js と npm の基本的な使い方
- iOS/Android/Webアプリのインストール方法
- E2E暗号化の基本概念（ペアリング、鍵交換）

## 根拠

> 「Mobile and Web Client for Claude Code & Codex」— 公式READMEより

> 「Use Claude Code or Codex from anywhere with end-to-end encryption.」— 公式説明

> 「npm install -g happy-coder」「happy」「happy codex」— インストール・実行手順

> 「📱 iOS App, 🤖 Android App, 🌐 Web App」— マルチプラットフォーム対応

> 「yarn cli --help」「yarn cli codex」— ソースから実行する方法
