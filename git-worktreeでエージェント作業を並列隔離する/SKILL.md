# git worktreeでエージェント作業を並列隔離する

> 各タスクを独立した git worktree ブランチで実行し、複数サブエージェントが同時並行で作業できる環境を構築する

- 出典: https://x.com/btcqzy1/status/2033116943712993717
- 投稿者: 爱丽丝呀！
- カテゴリ: agent-orchestration

## なぜ使うのか

複数タスクを同一ブランチで実行するとファイル競合や中途半端な状態のコードが混入する。worktreeで隔離することで安全な並列実行と後工程でのPRマージが可能になる

## いつ使うのか

実装計画が複数の独立したタスクに分割でき、並列実行が可能なとき。Claude Codeのサブエージェント機能を使うとき

### 具体的な適用場面

- 長期間・複数ファイルにわたる機能追加をAIエージェントに任せるとき
- AIが書いたコードがすぐにスパゲッティ化するプロジェクトで品質を安定させたいとき
- Claude Code / Cursor / Codex / Gemini CLI を使っているチームがテスト文化を強制したいとき

## やり方

1. SuperPowersが計画フェーズでタスクをファイルパス・コードスニペット単位まで分割する
2. 各タスクに対して `git worktree add ../task-branch-N -b feature/task-N` でworktreeを作成
3. 各サブエージェントが割り当てられたworktreeで独立してTDDサイクルを実行
4. 完了したworktreeのブランチからPRを自動作成
5. メインエージェントが各サブエージェントの進捗を監視・調整する

### 入力

- エージェントが生成したタスク分割計画
- gitリポジトリ

### 出力

- 各タスクに対応した独立ブランチ
- 完了後の自動PR

## 使うツール・ライブラリ

- git worktree
- SuperPowers
- Claude Code サブエージェント機能

## コード例

```
git worktree add ../task-branch-1 -b feature/task-1
git worktree add ../task-branch-2 -b feature/task-2
```

## 前提知識

- Claude Code・Cursor・Codex・Gemini CLI のいずれかのインストールと基本操作の習得
- git の基本操作（ブランチ・PR・worktree）
- TDD（テスト駆動開発）の概念理解

## 根拠

> 「7阶段强制流水线，缺一不可。脑暴+设计验证 → git worktree → 计划拆分 → 子Agent执行+TDD → 审查 → 完成分支/PR」

> 「先写测试、看它失败、再写代码、看它通过——跳过测试的代码直接删掉重来」

> 「每个任务完成后触发双阶段代码审查，先查规格符合度，再查代码质量，Critical 问题不解决不许前进」

> GitHub README: 「it launches a subagent-driven-development process, having agents work through each engineering task, inspecting and reviewing their work」

> GitHub README: 「It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY」
