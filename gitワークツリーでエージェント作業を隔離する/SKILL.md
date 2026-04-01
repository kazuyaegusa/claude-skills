# Gitワークツリーでエージェント作業を隔離する

> AIエージェントの作業を専用Gitブランチ＋独立したワークツリーディレクトリに閉じ込め、mainブランチと作業環境を物理的に分離する。

- 出典: https://x.com/jiroucaigou/status/2035964407201849564
- 投稿者: 努力赚钱的菜狗
- カテゴリ: agent-orchestration

## なぜ使うのか

AIが生成したコードが想定外の変更をしてもmainが汚染されない。問題があれば worktree ごと削除するだけで完全にリセットできる。複数エージェントが同じファイルを競合なしに並列編集できる。

## いつ使うのか

AIエージェントに独立した機能開発を任せるとき、複数エージェントを並列起動してそれぞれ別ファイルを触らせるとき

### 具体的な適用場面

- AIが生成したコードは動くが、プロジェクト拡大後に保守不能になるパターンが繰り返されているとき
- 要件が曖昧なままAIに着手させて後から仕様ズレが発覚するケースを防ぎたいとき
- 複数の独立機能を並列開発してAIの作業スループットを上げたいとき
- AIエージェントに数時間の自律作業をさせたいが品質保証が不安なとき

## やり方

1. `git worktree add -b feature-xxx /tmp/worktree-xxx main` でブランチと作業ディレクトリを同時作成。2. エージェントを `/tmp/worktree-xxx` で起動して作業させる。3. 作業完了後 `git worktree remove /tmp/worktree-xxx` で削除、または `git merge feature-xxx` でmainに取り込む。Superpowersインストール済みの場合は `superpowers:using-git-worktrees` スキルが自動でこの手順を実行する。

### 入力

- ブランチ名
- worktreeパス（例: /tmp/worktree-feature-auth）

### 出力

- 隔離されたGitブランチ
- 独立した作業ディレクトリ

## 使うツール・ライブラリ

- git worktree
- Superpowers
- superpowers:using-git-worktrees スキル

## コード例

```
git worktree add -b feature-xxx /tmp/worktree-xxx main
# エージェント作業後
git -C /tmp/worktree-xxx diff main
git worktree remove /tmp/worktree-xxx
```

## 前提知識

- Claude Code CLI または Cursor がインストール済みであること
- Gitの基本操作（branch, merge, worktree）を理解していること
- TDD（テスト駆動開発）の赤→緑サイクルの概念を知っていること

## 根拠

> 「1.先疯狂提问，把你的需求完全理解，你同意后并生成标准设计文档」—— 要件深掘りと設計文書生成の強制

> 「2.开新分支+隔离工作区，确保不会搞乱主代码」—— ブランチ+隔離ワークスペースの使用

> 「3.把任务拆分成最小子任务」—— 最小サブタスク分割

> 「4.交给子Agent执行并强制测试，最小代码也要通过测试」—— サブエージェントへの委任とテスト強制

> 「5.对完成的任务进行双重审查，不仅要符合设计规格，更要检查代码质量，有一项不过关就不放行」—— 仕様適合＋コード品質のダブルレビュー
