# タスクを最小単位に分割してサブエージェントに委任する

> 設計文書から実装タスクを最小のサブタスクに分解し、各タスクをサブエージェントに委任してTDD（Red/Green）で実行させる

- 出典: https://x.com/jiroucaigou/status/2035964407201849564
- 投稿者: 努力赚钱的菜狗
- カテゴリ: agent-orchestration

## なぜ使うのか

大きなタスクをAIに一度に渡すと判断が散漫になり品質が下がる。最小タスク単位での委任+テスト強制により、各ステップの成果を検証しながら前進できる

## いつ使うのか

設計文書が承認されてコーディングフェーズに入るとき。特にタスク間の依存関係が整理されている場合

### 具体的な適用場面

- プロジェクトが大きくなるにつれてAI生成コードの整合性が崩れてきた場合
- Claude CodeやCursorでエージェントに長時間タスクを委任したいが、途中で脱線するのを防ぎたい場合
- チームでAIコーディングを使うが、各自が独自プロセスで動いていて品質がばらつく場合

## やり方

1. SuperPowersの`subagent-driven-development`スキルが自動発火
2. 設計文書のタスクリストを1タスク=1サブエージェントに割り当て
3. 各サブエージェントは`test-driven-development`スキルに従い、まずテストを書いてから実装
4. テストがパスするまで実装を繰り返す（Red→Green）
5. 並列実行可能なタスクは`dispatching-parallel-agents`スキルで同時実行

### 入力

- 承認済み設計文書
- タスクリスト

### 出力

- テストが全てパスする実装コード
- 各タスクの完了ステータス

## 使うツール・ライブラリ

- superpowers subagent-driven-development skill
- superpowers test-driven-development skill
- superpowers dispatching-parallel-agents skill

## 前提知識

- Claude CodeまたはCursorのインストール
- gitの基本操作（branch・worktree）の理解
- TDD（テスト駆動開発）の基本概念

## 根拠

> SuperPowers is a complete software development workflow for your coding agents, built on top of a set of composable 'skills'

> it *doesn't* just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do

> It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY

> it launches a *subagent-driven-development* process, having agents work through each engineering task, inspecting and reviewing their work

> It's not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan
