# Agent Teamsでエージェント間直接メッセージングを実現する

> Claude Code Agent Teamsを使い、エージェントが共有タスクリストと直接メッセージングで連携する分散型マルチエージェントシステムを構築する

- 出典: https://x.com/akihiro_genai/status/2026078844814586041
- 投稿者: akihiro（あきひろ）| 生成AI活用
- カテゴリ: claude-code-workflow

## なぜ使うのか

スター型と異なりリードを介さずエージェント同士が直接情報交換できるため、相互依存するタスク（フロントエンド↔バックエンド等）での途中発見の即時共有と協調修正が可能になる

## いつ使うのか

フロント↔バックエンド協調開発など相互依存するタスクを複数エージェントに分担させる時、または途中の発見をエージェント間でリアルタイムに共有しながら協調させたい時

### 具体的な適用場面

- フロントエンドとバックエンドの実装を別エージェントに分担させ、API仕様変更をリアルタイムに相互反映させたい時（Agent Teams）
- コードレビュー・テスト・ドキュメント生成など独立した複数タスクを並列処理したい時（Codex Multi-Agents）
- メインコンテキストを消費せず単一タスクを隔離実行したい時（Subagent）

## やり方

1. Claude Code Agent TeamsのExperimental機能を有効化する（公式: code.claude.com/docs/en/agent-teams）。2. チームメンバーとなるエージェントを「Specify teammates and models」セクションの手順で定義・指定する。3. 各エージェントが共有タスクリストでタスクの割り当てと状態を管理する（「Assign and claim tasks」）。4. エージェント間の直接メッセージはSendMessageツールで送受信する。5. ユーザーも個別チームメイトに「Talk to teammates directly」で直接アクセス可能。6. 終了時は「Shut down teammates」→「Clean up the team」の順で片付ける。7. 品質ゲートはhooksで強制できる（「Enforce quality gates with hooks」）

### 入力

- チームで取り組む複合タスクの定義
- 各エージェントの役割定義
- Agent TeamsのExperimental機能が有効なClaude Code環境

### 出力

- 各エージェントの作業成果物
- リードエージェントによる統合結果

## 使うツール・ライブラリ

- Claude Code（claude CLI）
- Agent Teams（Experimental）
- SendMessageツール（Claude Code内蔵）

## コード例

```
# エージェント間の直接メッセージ送信（SendMessageツール）
SendMessage({to: 'backend-agent', message: 'APIレスポンス形式を{id, name, status}に変更したい'})
# 受け取ったバックエンドエージェントが直接返答可能
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
