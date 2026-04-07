# Status Lineによるリアルタイム監視

> Claude Codeのステータスバーに、使用中モデル、トークン消費量、コスト、gitブランチ、MCP接続状態などをリアルタイム表示

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeはデフォルトでトークン使用量やコストが見えず、気づかないうちに上限に達する。Status Lineで可視化することで予算管理と最適化が可能に

## いつ使うのか

トークン消費を厳密に管理したい、複数プロジェクトでコストを比較したい、Burn Rate（消費速度）を監視したい時

## やり方

1. Status Lineツール（CCometixLine、claudia-statusline等）をインストール
2. `~/.claude/statusline` に設定ファイルを配置
3. Claude Code起動時に自動表示
4. SQLite等で使用履歴を永続化し、セッション間で統計を追跡

### 入力

- Status Line設定ファイル
- オプションでSQLite DB（履歴保存）

### 出力

- リアルタイムのトークン・コスト表示
- セッション履歴と統計レポート

## 使うツール・ライブラリ

- CCometixLine（Rust製、高性能）
- claudia-statusline（永続化統計）
- claude-powerline（vim風デザイン）

## コード例

```
# 例: claudia-statuslineのステータス表示
[Sonnet-4.5] main | 12.5K↑ 3.2K↓ | $0.08 | 15% (2h left)
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
