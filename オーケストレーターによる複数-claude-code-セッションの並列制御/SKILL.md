# オーケストレーターによる複数 Claude Code セッションの並列制御

> 複数の Claude Code インスタンスを並列起動し、異なるタスク（フロントエンド開発、バックエンド開発、テストなど）を同時進行させる

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

1 つの Claude Code セッションで複数の独立したタスクを順次処理すると時間がかかる。並列実行することで開発速度を大幅に向上できるため

## いつ使うのか

大規模プロジェクトで複数の独立したタスクを同時進行させたい時、チーム開発で役割分担したい時

## やり方

1. オーケストレーターツール（Auto-Claude、Claude Squad など）をインストール
2. タスクごとにワークスペースを分割
3. 各ワークスペースで Claude Code セッションを起動
4. オーケストレーターの UI でタスクの進捗を監視
5. 完了したタスクの成果物を統合

### 入力

- タスク定義（フロントエンド、バックエンド、テストなど）
- ワークスペース設定

### 出力

- 並列実行されたタスクの成果物
- 統合されたコードベース

## 使うツール・ライブラリ

- Auto-Claude（マルチエージェント SDLC）
- Claude Squad（複数エージェント管理）
- TSK（Docker サンドボックス並列実行）
- sudocode（軽量オーケストレーター）

## 前提知識

- Claude Code の基本的な使い方（インストール、セッション開始、プロンプト入力）
- Git の基礎知識（コミット、ブランチ、PR 作成）
- Markdown の基本文法
- シェルスクリプト（Bash）の基礎知識（フック・スラッシュコマンドのカスタマイズに必要）
- JSON の基本構造（フック設定ファイルの編集に必要）

## 根拠

> "A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow."

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"
