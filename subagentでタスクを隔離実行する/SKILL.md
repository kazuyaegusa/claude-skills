# Subagentでタスクを隔離実行する

> メインセッションから単一タスクを独立したコンテキストのSubagentに委譲し、結果だけをメインに返す（ワンショット型）

- 出典: https://x.com/akihiro_genai/status/2026078844814586041
- 投稿者: akihiro（あきひろ）| 生成AI活用
- カテゴリ: agent-orchestration

## なぜ使うのか

メインコンテキストを汚さずタスクを処理できる。唯一のStable正式機能であり、今すぐ本番投入できる

## いつ使うのか

コードレビュー・ファイル解析・単一API呼び出しなど明確に区切られたタスクをメインコンテキストから切り離したい時

### 具体的な適用場面

- フロントエンドとバックエンドの実装を別エージェントに分担させ、API仕様変更をリアルタイムに相互反映させたい時（Agent Teams）
- コードレビュー・テスト・ドキュメント生成など独立した複数タスクを並列処理したい時（Codex Multi-Agents）
- メインコンテキストを消費せず単一タスクを隔離実行したい時（Subagent）

## やり方

1. `~/.claude/agents/` ディレクトリにYAMLフロントマター付きMarkdownファイルを作成する。2. `/agents` コマンドでサブエージェント一覧と管理UIを開く。3. メインセッション内でAgentツールを呼び出す際に `subagent_type` パラメータで対象を指定する。4. 結果はメインセッションに文字列として返却される。設定例: `---
name: code-reviewer
description: コードレビュー専門エージェント
model: claude-opus-4-6
---`

### 入力

- 委譲タスクの定義テキスト
- YAMLフロントマター付きエージェント定義ファイル

### 出力

- タスク実行結果テキストがメインセッションに返却される

## 使うツール・ライブラリ

- Claude Code
- Agentツール（Claude Code内蔵）

## コード例

```
---
name: code-reviewer
description: コードレビュー専門エージェント
model: claude-sonnet-4-6
---
# Code Reviewer
コードレビューを行う専門エージェント。
```

## 前提知識

- Claude Code または Codex の基本的な使い方
- Subagentの概念（タスク委譲と結果返却の基本形）の理解
- Agent Teams / Codex Multi-AgentsはExperimentalフィーチャーのため有効化が必要

## 根拠

> 「SubagentsだけがStableな正式機能で、これから紹介するMulti-AgentsとAgent Teamsはどちらもまだ実験段階（Experimental）」

> 「公式ドキュメントにも「routing follow-up instructions」（追加指示のルーティング）と明記されていて、エージェントがスレッドとして存続し続ける」

> 「公式では「Ask Codex directly to steer a running sub-agent, stop it, or close completed agent threads」と書かれていて」

> 「エージェント同士が直接やり取りすることはない。A・B・Cがそれぞれ並列で動いていても、Aの発見をBが直接知ることはない」（Multi-Agentsの制約）

> 「チームメイトがリードを介さずに直接メッセージを送り合える」（Agent Teamsの特徴）
