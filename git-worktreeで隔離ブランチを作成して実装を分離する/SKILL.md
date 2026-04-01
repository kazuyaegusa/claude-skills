# git worktreeで隔離ブランチを作成して実装を分離する

> タスク実装前に新しいブランチとgit worktreeを作成し、mainブランチのコードを汚さない隔離環境で作業する

- 出典: https://x.com/jiroucaigou/status/2035964407201849564
- 投稿者: 努力赚钱的菜狗
- カテゴリ: agent-orchestration

## なぜ使うのか

AIが生成したコードが意図しない影響を与えても、worktreeが隔離されているためmainブランチは安全。並列サブエージェントがそれぞれ独立した作業空間を持てる

## いつ使うのか

サブエージェントに並列でタスクを委任するとき、またはmainブランチを安全に保ちたいコーディングタスク全般

### 具体的な適用場面

- Claude Code / Cursorで新機能を実装しようとするたびにAIが設計なしに書き始めて後悔する状況
- チームでAIコーディングを使っているが、各人がバラバラなプロンプト戦略を取っていて品質が安定しない状況
- AIが生成したコードが動くが後のリファクタ・バグ修正が困難になっているプロジェクト

## やり方

1. SuperPowersのusing-git-worktreesスキルが自動起動
2. `git worktree add ../project-feature-branch feature-branch` でworktreeを作成
3. 各サブエージェントは独立したworktreeディレクトリで作業
4. 完了後に `git worktree remove` でクリーンアップ

### 入力

- git管理されたプロジェクト
- 実装するタスクのブランチ名

### 出力

- 隔離されたworktreeディレクトリ
- mainブランチに影響しない実装環境

## 使うツール・ライブラリ

- git worktree
- obra/superpowers (using-git-worktreesスキル)

## コード例

```
git worktree add ../project-feature-branch feature-branch
```

## 前提知識

- Claude Code または Cursor が動作する環境
- Node.js / npx が使える環境（CLIインストールの場合）
- git が使える環境（worktree機能のため）
- AIコーディングエージェントの基本的な使い方を知っていること

## 根拠

> 「SuperPowers制定了一套规则，让AI可以像资深团队一样有一套标准的开发流程。目前已在Github斩获106kstars」

> 「1.先疯狂提问，把你的需求完全理解，你同意后并生成标准设计文档」

> 「2.开新分支+隔离工作区，确保不会搞乱主代码」

> 「3.把任务拆分成最小子任务」

> 「4.交给子Agent执行并强制测试，最小代码也要通过测试」
