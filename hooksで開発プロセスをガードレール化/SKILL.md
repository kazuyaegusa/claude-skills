# Hooksで開発プロセスをガードレール化

> Claude Codeのライフサイクルイベント（ファイル書き込み前、Bash実行前等）に自動チェック・承認ロジックを挿入する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

危険なコマンド実行やTDD違反、プロンプトインジェクション攻撃を事前に防ぎ、安全性と品質を保証するため

## いつ使うのか

危険なコマンド（rm -rf等）の自動承認を防ぎたいとき、TDDプロセスを強制したいとき、シークレット漏洩をリアルタイム検出したいとき

## やり方

1. リストからHooksツール（例：Dippy、parry、TDD Guard）を選択
2. `~/.claude/hooks.json`に該当フックを登録
3. フックスクリプトを配置（例：Bash AST解析スクリプト、SHA256キャッシュ型リンタースクリプト）
4. Claude Codeが該当イベント時にフックを自動実行
5. フック結果に応じて処理続行/ブロック/ユーザー確認要求

### 入力

- フック種別（user-prompt-submit、tool-input、tool-output等）
- チェックロジック（AST解析、正規表現、LLM判定等）

### 出力

- 安全性が保証された実行フロー
- ブロック/承認/警告メッセージ

## 使うツール・ライブラリ

- Dippy（AST解析による安全コマンド自動承認）
- parry（プロンプトインジェクションスキャナー）
- TDD Guard（TDD原則違反を検出）

## 前提知識

- Claude Codeの基本的な使い方（CLIでの起動、プロンプト入力、ファイル操作）
- Git、GitHub、PR、Issueなどの基本概念
- JSONファイルの編集（hooks.json等の設定）
- ターミナル操作、シェルスクリプトの基礎
- （リソースによって）Docker、Node.js、Python、Rust等の環境構築知識

## 根拠

> > A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task

> CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards
