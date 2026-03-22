# Orchestratorsによる並列マルチエージェント実行

> 複数のClaude Codeインスタンスを並列実行し、タスクを分散処理してから結果を統合する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

大規模なプロジェクトでは、1つのClaude Codeインスタンスで全てを処理すると時間がかかりすぎる。複数エージェントに分割して並列実行することで、10倍以上の高速化が可能になる

## いつ使うのか

複数の独立したタスクがあり、並列実行で時間を短縮したい場合（例：複数モジュールの同時開発、大量のテストケース生成、複数APIエンドポイントの実装）

## やり方

1. オーケストレータツール（Auto-Claude、Claude Squad、TSK等）をインストール
2. タスクを独立した単位に分割（例：モジュールごと、機能ごと）
3. 各タスクを別々のClaude Codeインスタンス（Dockerコンテナやtmuxセッション）に割り当て
4. 並列実行し、完了を待つ
5. 結果を統合（例：各エージェントがgit branchを作成→人間がレビュー→マージ）

例：TSKは各タスクをDockerサンドボックス内で実行し、完了後にgit branchとして返す

### 入力

- タスク定義（JSON、YAML等）
- オーケストレータ設定ファイル
- 実行環境（Docker、tmux等）

### 出力

- 各エージェントが生成したコード（git branch形式等）
- 統合レポート
- 並列実行ログ

## 使うツール・ライブラリ

- Auto-Claude（SDLCフルサイクル、kanban UI）
- Claude Squad（複数ワークスペース管理）
- TSK（Dockerサンドボックス、git branch返却）
- Happy Coder（モバイル通知、並列実行）

## コード例

```
# TSK example
tsk run \
  --task "Implement user authentication module" \
  --task "Implement payment processing module" \
  --task "Implement notification system" \
  --parallel 3 \
  --output branches
```

## 前提知識

- Claude Codeの基本的な使い方（CLI操作、プロンプト入力、ファイル編集）
- Gitの基礎知識（branch、commit、PR）
- シェルスクリプト/Python/Node.jsの基礎（Hooks実装時）
- Docker/tmuxの基礎知識（Orchestrators使用時）
- JSON/YAML形式の理解（設定ファイル編集時）
