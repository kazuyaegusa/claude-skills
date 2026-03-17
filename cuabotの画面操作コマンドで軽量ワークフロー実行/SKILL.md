# CuaBotの画面操作コマンドで軽量ワークフロー実行

> LLMエージェントを使わず、cuabotコマンド単体でスクリーンショット・クリック・タイプ操作を実行する

- 出典: https://github.com/trycua/cua
- 投稿者: trycua
- カテゴリ: agent-orchestration

## なぜ使うのか

単純な操作手順が決まっている場合、LLM推論のオーバーヘッドなしで高速・確実に実行したいため

## いつ使うのか

決まった手順を繰り返し実行する軽量RPA的なタスク、またはエージェント開発時のデバッグ操作

## やり方

1. `cuabot chromium` でサンドボックス内Chromium起動
2. `cuabot --screenshot` で画面キャプチャ
3. `cuabot --type "hello"` でテキスト入力
4. `cuabot --click <x> <y> [button]` で座標クリック

### 入力

- 操作対象アプリ名（chromium等）
- 座標・テキスト等のパラメータ

### 出力

- 実行結果（スクリーンショット画像、クリック成否等）

## 使うツール・ライブラリ

- cuabot CLI

## コード例

```
cuabot chromium
cuabot --screenshot
cuabot --type "hello"
cuabot --click <x> <y> [button]
```

## 前提知識

- Python 3.12または3.13（Cua Agent SDK使用時）
- Node.js環境（CuaBot使用時）
- Apple Silicon Mac（Lume使用時）
- LLM APIアクセス（Anthropic Claude等、エージェント実行時）
- Computer-Use AgentやRPA/自動化の基本概念理解
