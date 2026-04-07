# Alternative Clientsによるモバイル・リモート管理

> モバイルやWebブラウザから複数のClaude Codeセッションをリモート監視・操作できるクライアントアプリを使用

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

開発マシンから離れている時でも、Claude Codeの進捗確認や緊急対応が必要な場合がある。リモートクライアントで場所を問わず管理可能に

## いつ使うのか

外出中にClaude Codeのタスク完了を確認したい、複数セッションを並行監視したい、チームで進捗を共有したい時

## やり方

1. Alternative Client（Omnara、Happy Coder等）をインストール
2. Claude Codeセッションとクライアントを連携（WebSocket/HTTP経由）
3. モバイル・Webからセッション一覧を表示
4. 承認待ちタスクに対してプッシュ通知→モバイルから承認/却下
5. 完了時に結果を確認・マージ

### 入力

- Claude Codeセッション（バックグラウンド実行）
- クライアントアプリ（Omnara等）

### 出力

- リモートからのセッション監視・操作
- プッシュ通知でタスク完了を即座に把握

## 使うツール・ライブラリ

- Omnara（Web/モバイル統合管理）
- Happy Coder（プッシュ通知対応）
- crystal（デスクトップアプリ）

## コード例

```
# 例: Omnaraでセッション起動
omnara start --session backend-api
# → モバイルで進捗確認
# → 承認待ち → スマホで承認 → 自動継続
```

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ツール実行）
- Git/GitHubの基礎知識（ブランチ、コミット、PR）
- ターミナル操作とシェルスクリプトの基本
- Markdown記法の理解
- 使用する言語・フレームワークの基礎知識（TypeScript、Python、Go等）

## 根拠

> 「A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow」

> 「Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities」

> 「Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle」

> 「Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task」

> 「CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards」
