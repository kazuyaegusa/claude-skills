# 非対話モードでスクリプトから呼び出し、JSON出力を取得

> `-p` フラグでプロンプトを指定し、`--output-format json` で構造化された応答を取得する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

自動化パイプラインやCIでLLMを呼び出す際、標準出力をパース可能な形式で取得することで後続処理を実装できる

## いつ使うのか

CI/CDでコードレビューやテスト結果の要約を自動生成する時、cron等でLLMに定期タスクを実行させる時

## やり方

1. `gemini -p "質問内容" --output-format json` を実行
2. 標準出力に返されるJSONを `jq` 等でパース
3. エラーハンドリングのため終了コードを確認
4. リアルタイム監視が必要な場合は `--output-format stream-json` で逐次イベントを取得

### 入力

- プロンプト文字列
- 必要に応じてコンテキストファイル（GEMINI.md）

### 出力

- JSON形式の応答（text, tool_calls等）
- 終了コード（成功=0, エラー=非0）

## 使うツール・ライブラリ

- Gemini CLI
- jq（JSON処理）
- Bash/Python等のスクリプト言語

## コード例

```
gemini -p "Explain the architecture of this codebase" --output-format json | jq '.response.text'
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

> 「Non-interactive mode for scripts: gemini -p 'Explain the architecture of this codebase' --output-format json」（スクリプト向け非対話モード、JSON出力）
