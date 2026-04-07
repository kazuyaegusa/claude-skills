# 基本ツール（検索・ファイル操作・シェル）を選択的に無効化

> search_for_pattern, replace_content, list_dir, find_file, read_file, execute_shell_commandを設定で無効化可能

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude CodeやCodexなど既にこれらの機能を持つハーネス内で使う場合、ツールの重複を避けて認知負荷とトークン消費を削減。

## いつ使うのか

Serenaをエージェントハーネス（Claude Code/Codex）と併用する時

## やり方

1. クライアント用の設定モードを作成 2. 重複するツールを `enabled: false` に設定 3. MCP起動コマンドで `-m <mode>` を指定

### 入力

- クライアント機能マップ

### 出力

- 重複なしのツールセット

## 使うツール・ライブラリ

- Serena設定システム

## 前提知識

- Model Context Protocol (MCP)の基本的な理解
- Language Server Protocol (LSP)の概念
- uv (Pythonパッケージマネージャ)の使い方
- シンボル・参照・型階層などのIDE概念
- Claude Code/Codex/Claude Desktop等のMCP対応クライアント
