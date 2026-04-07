# Multi-agent Orchestrationによる並列タスク実行

> 複数のClaude Codeインスタンスを並列起動し、Task Masterが各エージェントにサブタスクを割り当て、結果を統合する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

大規模プロジェクトでは単一エージェントでは時間がかかりすぎる。複数エージェントで並列処理することで開発速度を劇的に向上

## いつ使うのか

複数の独立した機能を同時開発、大規模リファクタリング、並列テスト実行、複数ブランチでの実験が必要な時

## やり方

1. オーケストレーターツール（Claude Squad、Ruflo、TSK等）をインストール
2. タスクをサブタスクに分解（例: 「認証機能実装」→「フロントエンド」「バックエンド」「テスト」）
3. 各サブタスクを独立したClaude Codeインスタンスに割り当て
4. Docker/git worktreeで隔離された環境を提供
5. 完了後、オーケストレーターが結果をマージ・検証

### 入力

- 親タスクの要件定義
- サブタスク分解ロジック

### 出力

- 各エージェントが生成したコード・PRを統合
- 並列実行による大幅な時間短縮

## 使うツール・ライブラリ

- Claude Squad（複数Claude Code/Codexを同時管理）
- Ruflo（自律マルチエージェントスウォーム）
- TSK（Docker隔離環境でタスク並列実行）

## コード例

```
# 例: Claude Squadで3つのタスクを並列実行
claudesquad start
# → ターミナルUIで複数ワークスペース管理
# Workspace 1: 認証API実装
# Workspace 2: フロントエンドUI
# Workspace 3: E2Eテスト作成
```

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ツール実行）
- Git/GitHubの基礎知識（ブランチ、コミット、PR）
- ターミナル操作とシェルスクリプトの基本
- Markdown記法の理解
- 使用する言語・フレームワークの基礎知識（TypeScript、Python、Go等）

## 根拠

> 「Multi-agent Orchestration - Launch Claude Code session that is connected to a swarm of Claude Code Agents」
