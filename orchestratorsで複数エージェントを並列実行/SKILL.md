# Orchestratorsで複数エージェントを並列実行

> 複数のClaude Codeインスタンスを並列・階層的に管理し、大規模タスクを分散処理

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一セッションではコンテキスト制限やタスク複雑度で限界があるため、複数エージェントで分業することで効率と品質を向上させるため

## いつ使うのか

大規模リファクタリング、複数モジュールの同時開発、並列テスト実行など、独立した複数タスクを効率的に処理したいとき

## やり方

1. Orchestratorツール（例：Auto-Claude、Claude Squad、Happy Coder）をインストール
2. タスクを独立したサブタスクに分解
3. 各サブタスクを別々のClaude Codeインスタンスに割り当て
4. Orchestratorが進捗監視・結果統合・エラーハンドリングを実行
5. 完了後、各エージェントの成果物を統合

### 入力

- 分割されたサブタスク群
- 各タスクの入力コンテキスト

### 出力

- 並列実行された成果物群
- 統合されたプロジェクト成果

## 使うツール・ライブラリ

- Auto-Claude
- Claude Squad
- Claude Swarm
- Happy Coder

## 前提知識

- Claude Codeの基本的な使い方（CLIでの起動、プロンプト入力、ファイル操作）
- Git、GitHub、PR、Issueなどの基本概念
- JSONファイルの編集（hooks.json等の設定）
- ターミナル操作、シェルスクリプトの基礎
- （リソースによって）Docker、Node.js、Python、Rust等の環境構築知識
