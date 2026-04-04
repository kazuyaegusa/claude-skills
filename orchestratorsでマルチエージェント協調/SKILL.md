# Orchestratorsでマルチエージェント協調

> 複数のClaude Codeインスタンスを並列実行し、タスクを分散・協調させるツールを使う

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

大規模タスクを分割して並列処理することで、開発速度を劇的に向上できる。各エージェントが独立したコンテキストで作業するため、コンテキスト制限を回避できる。

## いつ使うのか

大規模リファクタリング、複数機能の並行開発、コードベース全体の分析など、単一エージェントでは時間がかかりすぎるタスク

## やり方

1. Ruflo、Auto-Claude、Claude Squad等のツールをインストール
2. タスクを複数のサブタスクに分割
3. 各サブタスクを別々のClaude Codeインスタンスに割り当て
4. オーケストレーターがエージェント間の調整・結果統合を実施

### 入力

- 大規模タスク
- タスク分割戦略

### 出力

- 並列実行された結果
- 統合されたアウトプット

## 使うツール・ライブラリ

- Ruflo
- Auto-Claude
- Claude Squad
- TSK

## 前提知識

- Claude Codeの基本的な使い方（CLI操作、セッション管理）
- Gitの基礎知識（ブランチ、コミット、PR等）
- シェルスクリプトまたはPython/TypeScriptの基礎（Hook・Skill作成に必要）
- プロジェクトのビルド・テストコマンドの理解
