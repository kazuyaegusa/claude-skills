# 要件ヒアリングからspec文書を生成する

> コーディング開始前にエージェントが徹底的な質問を行い、ユーザー確認後に標準設計文書を自動生成する

- 出典: https://x.com/jiroucaigou/status/2035964407201849564
- 投稿者: 努力赚钱的菜狗
- カテゴリ: agent-orchestration

## なぜ使うのか

仕様の曖昧さを事前に排除することで、実装中の手戻りや「動くけど要求と違う」問題を防ぐ。設計文書がチェックポイントとして機能し、後の二重レビューの基準になる

## いつ使うのか

新機能追加・バグ修正・リファクタリング等、コーディングタスクを開始するとき全般

### 具体的な適用場面

- プロジェクトが大きくなるにつれてAI生成コードの整合性が崩れてきた場合
- Claude CodeやCursorでエージェントに長時間タスクを委任したいが、途中で脱線するのを防ぎたい場合
- チームでAIコーディングを使うが、各自が独自プロセスで動いていて品質がばらつく場合

## やり方

1. SuperPowersインストール済み環境でタスクを投げると、エージェントが自動で`brainstorming`スキルを発火
2. エージェントが「何のために？」「誰が使う？」「成功状態は？」等の質問を順次する
3. 回答内容を元にエージェントがspec文書（設計仕様）を生成・提示
4. ユーザーが承認するまでコーディングに進まない（`writing-plans`スキルが制御）

### 入力

- 実現したい機能の概要（箇条書きレベルで可）

### 出力

- 設計仕様文書（実装計画・タスク一覧・完了条件を含む）

## 使うツール・ライブラリ

- superpowers brainstorming skill
- superpowers writing-plans skill

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
