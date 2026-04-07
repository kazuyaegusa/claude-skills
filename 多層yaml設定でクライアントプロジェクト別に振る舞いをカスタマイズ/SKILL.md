# 多層YAML設定でクライアント・プロジェクト別に振る舞いをカスタマイズ

> グローバル設定、CLI設定、プロジェクト設定、実行コンテキスト設定、動的モード設定の5層で構成可能な設定システム

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude CodeとClaude Desktopではツールの重複範囲が異なる、プロジェクトによって使う言語が違うなど、単一設定では対応不可能なユースケースに柔軟に対応。

## いつ使うのか

複数クライアント対応、プロジェクト固有のツール有効化、特定言語バックエンドの切り替えが必要な時

## やり方

1. `~/.config/serena/config.yaml` にグローバル設定を記述 2. プロジェクトルートに `.serena/config.yaml` を配置してローカルオーバーライド 3. MCP起動コマンドで `-m <mode>` を指定して動的に設定を合成

### 入力

- YAML設定ファイル（グローバル・プロジェクト別・モード別）

### 出力

- 実行時に合成された最終設定

## 使うツール・ライブラリ

- YAML
- Serena設定システム

## 前提知識

- Model Context Protocol (MCP)の基本的な理解
- Language Server Protocol (LSP)の概念
- uv (Pythonパッケージマネージャ)の使い方
- シンボル・参照・型階層などのIDE概念
- Claude Code/Codex/Claude Desktop等のMCP対応クライアント
