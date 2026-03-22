# git worktreeベースのエージェント分離実行

> 各タスクを独立したgit worktree（別ディレクトリ＋ブランチ）に配置し、複数のCLIエージェントを同時並行で動かす

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

通常のエージェント実行では単一セッションしか動かせず、待ち時間が発生する。worktreeで物理的に分離すれば、ファイル競合やブランチ衝突なく10個以上のエージェントを同時実行でき、開発速度が飛躍的に向上する

## いつ使うのか

複数のタスクが独立しており、並行実行してもコンフリクトしない場合。または、タスク間に依存があっても順次マージで解消できる場合

## やり方

1. Supersetをインストール（macOS用ビルド版 or ソースビルド）
2. プロジェクトを開き「New workspace」（⌘N）でタスク1を作成
3. workspace内でCLIエージェント（claude-code等）を起動してタスク指示
4. ⌘⇧Nで次のworkspaceを作成、別のタスクを並行開始
5. ⌘1-9でworkspace切り替え、各エージェントの進捗を監視
6. 変更準備完了時に通知受信→diff viewerでレビュー
7. ⌘Oでエディタに開いて最終調整、またはそのままマージ

### 入力

- git管理されたプロジェクト
- Bun v1.0+, Git 2.20+, GitHub CLI, Caddy（開発時）
- macOS環境（Windows/Linux未検証）
- CLIで動作するエージェント（Claude Code, Codex, Gemini CLI等）

### 出力

- 各worktreeに独立したブランチ＋変更差分
- diff viewerで確認可能なコミット
- エディタまたはターミナルへのワンクリック遷移

## 使うツール・ライブラリ

- Superset（Electron製デスクトップアプリ）
- git worktree
- 任意のCLIエージェント（Claude Code、Codex、Cursor Agent、Gemini CLI等）

## 前提知識

- git worktreeの基本概念（1つのリポジトリから複数の作業ディレクトリを作成できる）
- CLIエージェント（Claude Code、Codex等）の基本的な使い方
- git操作の基礎（branch、merge、diff）
- macOS環境（現時点ではWindows/Linux未対応）
- Bun、Git 2.20+、GitHub CLIのインストール

## 根拠

> 「Isolate each task in its own git worktree so agents don't interfere with each other」
