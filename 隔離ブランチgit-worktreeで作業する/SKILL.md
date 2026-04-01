# 隔離ブランチ+git worktreeで作業する

> タスク開始時に新規ブランチを切り、git worktreeで隔離された作業環境を作成してメインコードへの影響を防ぐ

- 出典: https://x.com/jiroucaigou/status/2035964407201849564
- 投稿者: 努力赚钱的菜狗
- カテゴリ: agent-orchestration

## なぜ使うのか

複数のサブエージェントが並列作業する際、ブランチ・ワークツリーを分離することでコンフリクトや誤作動による主線コード汚染を防ぐ

## いつ使うのか

並列サブエージェントを使うとき、または独立した機能を安全に開発したいとき

### 具体的な適用場面

- プロジェクトが大きくなるにつれてAI生成コードの整合性が崩れてきた場合
- Claude CodeやCursorでエージェントに長時間タスクを委任したいが、途中で脱線するのを防ぎたい場合
- チームでAIコーディングを使うが、各自が独自プロセスで動いていて品質がばらつく場合

## やり方

1. SuperPowersが`using-git-worktrees`スキルを自動発火
2. 自動で`git worktree add ../feature-branch-name feature/xxx`を実行
3. 各サブエージェントは専用ワークツリー内でのみ作業
4. 完了後に`git worktree remove`でクリーンアップ
5. 手動でやる場合: `git worktree add -b feature/xxx ../worktrees/xxx origin/main`

### 入力

- gitリポジトリ
- 作業対象タスク名

### 出力

- メインブランチから隔離された作業ディレクトリ
- 安全にマージ可能なfeatureブランチ

## 使うツール・ライブラリ

- git worktree
- superpowers using-git-worktrees skill

## コード例

```
git worktree add -b feature/xxx ../worktrees/xxx origin/main
```

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
