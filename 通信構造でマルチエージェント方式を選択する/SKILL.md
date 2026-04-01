# 通信構造でマルチエージェント方式を選択する

> タスクの相互依存性と必要な通信パターンに応じて3方式（Subagent/Multi-Agents/Agent Teams）を判断基準に従って使い分ける

- 出典: https://x.com/akihiro_genai/status/2026078844814586041
- 投稿者: akihiro（あきひろ）| 生成AI活用
- カテゴリ: agent-orchestration

## なぜ使うのか

各方式の通信構造の違いを理解して選択することで、不要なオーバーヘッドを避けつつタスクに最適な情報フローを実現できる

## いつ使うのか

マルチエージェントシステムの設計時、またはタスクの複雑さと相互依存性に応じて適切な実行方式を選定する必要がある時

### 具体的な適用場面

- フロントエンドとバックエンドの実装を別エージェントに分担させ、API仕様変更をリアルタイムに相互反映させたい時（Agent Teams）
- コードレビュー・テスト・ドキュメント生成など独立した複数タスクを並列処理したい時（Codex Multi-Agents）
- メインコンテキストを消費せず単一タスクを隔離実行したい時（Subagent）

## やり方

以下の判断木で選択する: 1. 単一タスクを隔離したい → Subagent（Stable、今すぐ本番使用可）。2. 複数の独立タスクを並列処理したい（エージェント間通信不要）→ Codex Multi-Agents（Experimental）。3. 相互依存するタスクでエージェント間のリアルタイム情報共有が必要 → Claude Code Agent Teams（Experimental）。注意: Multi-AgentsとAgent TeamsはどちらもExperimentalのため本番投入は慎重に

### 入力

- 実行タスクの数と相互依存性の評価
- 本番/実験環境の制約確認

### 出力

- 選択した方式に基づくエージェント設計方針

## 使うツール・ライブラリ

- Claude Code Subagents（Stable）
- Codex Multi-Agents（Experimental）
- Claude Code Agent Teams（Experimental）

## コード例

```
# 判断フロー
# 単一タスク隔離 → Subagent (Stable)
# 独立並列タスク → Codex Multi-Agents (Experimental)
# 相互依存タスク → Agent Teams (Experimental)
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
