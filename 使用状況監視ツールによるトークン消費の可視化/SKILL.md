# 使用状況監視ツールによるトークン消費の可視化

> Claude Code のログファイルを解析し、トークン消費量・コスト・セッション履歴などをダッシュボードで可視化する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

無意識のうちにトークンを大量消費してしまうと、コストが跳ね上がったり、レート制限に引っかかったりするため、使用状況を監視して最適化が必要

## いつ使うのか

コスト管理が必要な時、チーム全体の使用状況を把握したい時、レート制限を回避したい時

## やり方

1. ccflare / ccusage などのツールをインストール
2. Claude Code のログファイル（~/.claude/logs/）を監視対象に設定
3. Web ダッシュボードまたは CLI でトークン消費量・コスト・セッション履歴を確認
4. 消費量が多いセッションを特定し、プロンプトを最適化

### 入力

- Claude Code ログファイル（JSONL 形式）

### 出力

- トークン消費量グラフ
- コスト予測
- セッション履歴

## 使うツール・ライブラリ

- ccflare（Web UI、Tableau 級の UI）
- better-ccflare（ccflare の拡張版）
- ccusage（CLI ダッシュボード）
- Claude Code Usage Monitor（リアルタイム監視）

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
