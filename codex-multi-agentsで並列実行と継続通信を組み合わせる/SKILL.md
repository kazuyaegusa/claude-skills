# Codex Multi-Agentsで並列実行と継続通信を組み合わせる

> 複数のエージェントを同時並列で走らせ、全完了を待って統合レスポンスを返しつつ、実行中エージェントへの追加指示・停止・クローズを親エージェント経由で動的に制御する

- 出典: https://x.com/akihiro_genai/status/2026078844814586041
- 投稿者: akihiro（あきひろ）| 生成AI活用
- カテゴリ: agent-orchestration

## なぜ使うのか

独立した複数タスクを直列でなく並列処理することで時間を短縮できる。さらにワンショット型と異なりエージェントがスレッドとして存続するため、中間結果を受けて追加調査を動的に指示できる

## いつ使うのか

独立した複数タスク（例: 複数ファイルの並列解析）を処理したい時、または実行中に動的に指示を変更・追加したい時

### 具体的な適用場面

- フロントエンドとバックエンドの実装を別エージェントに分担させ、API仕様変更をリアルタイムに相互反映させたい時（Agent Teams）
- コードレビュー・テスト・ドキュメント生成など独立した複数タスクを並列処理したい時（Codex Multi-Agents）
- メインコンテキストを消費せず単一タスクを隔離実行したい時（Subagent）

## やり方

1. Codex UIでExperimentalのMulti-Agents機能を有効化する。2. 並列実行したいタスクを複数サブエージェントに分散してキックする。3. 実行中エージェントへの追加指示は親（Codex）に対して「routing follow-up instructions」として送る（例: 「Aエージェントの結果を踏まえてBに追加調査させて」）。4. 実行中エージェントの操作は「Ask Codex directly to steer a running sub-agent, stop it, or close completed agent threads」で行う。5. エージェント間の直接通信はないため、間接共有は親経由でのみ可能

### 入力

- 並列化可能な独立タスクのリスト
- 各サブエージェントへの初期指示

### 出力

- 複数エージェントの実行結果を統合したレスポンス

## 使うツール・ライブラリ

- Codex（OpenAI）
- Codex Multi-Agents（Experimental）

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
