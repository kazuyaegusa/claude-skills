# オーケストレータによるマルチエージェント協調

> 複数のClaude Codeインスタンスを並列起動し、タスクを分散実行・結果を統合する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一エージェントのコンテキスト制約を回避し、大規模タスク（全ファイル監査、並列テスト実行等）を高速化できる

## いつ使うのか

モノレポで複数パッケージを同時変更、大量ファイルの一括リファクタリング、並列テスト実行が必要な時

## やり方

1. オーケストレータツール（Claude Squad, Auto-Claude, Ruflo等）をインストール
2. タスクを独立したサブタスクに分割（例: ファイルごとのリファクタリング）
3. 各サブタスクを別のClaude Codeインスタンス（Dockerコンテナまたはgit worktree）に割り当て
4. 各エージェントの実行結果を収集・マージ
5. 例: Claude Squadは複数ワークスペースで同時開発→最後にPRマージ

### 入力

- 分割可能な大規模タスク
- オーケストレータ設定（エージェント数、ワークスペース等）

### 出力

- 各エージェントの実行結果
- 統合されたPRまたは成果物

## 使うツール・ライブラリ

- Claude Squad（マルチワークスペース管理）
- Auto-Claude（SDLC統合）
- Ruflo（マルチエージェントswarm）
- viwo-cli（Docker + git worktree）

## コード例

```
# viwo-cli 例（Docker worktree起動）
viwo start feature/auth --dangerously-skip-permissions
viwo start feature/ui --dangerously-skip-permissions
# 各worktreeで独立してClaude Code実行
```

## 前提知識

- Claude Codeの基本的な使い方（セッション開始、ファイル編集、Bash実行）
- Gitの基礎知識（ブランチ、コミット、PR）
- JSON/YAML形式の理解（設定ファイル記述用）
- （オーケストレータ使用時）Dockerまたはgit worktreeの知識
- （言語特化CLAUDE.md使用時）対象言語のビルドツール知識（pnpm, Gradle, cargo等）

## 根拠

> 「Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.」

> 「Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.」

> 「Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task」

> 「CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards」

> 「ccflare - Claude Code usage dashboard with a web-UI that would put Tableau to shame. Thoroughly comprehensive metrics, frictionless setup, detailed logging, really really nice UI.」
