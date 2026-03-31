# 設定ファイルなしのコード直接カスタマイズ

> 設定ファイルを用意せず、ユーザーがコードを直接変更することでカスタマイズする

- 出典: https://github.com/qwibitai/nanoclaw
- 投稿者: qwibitai
- カテゴリ: claude-code-workflow

## なぜ使うのか

設定ファイルが増えると管理が複雑化し、結局コードを読まないと挙動が理解できなくなる。コードベースが十分小さければ、コード変更が最もシンプルで透明性の高いカスタマイズ手段になる

## いつ使うのか

フレームワークの挙動をカスタマイズしたいが、設定ファイルの複雑さを避けたい時。コードレビューが可能な規模のプロジェクトで

## やり方

1. ユーザーがClaude Codeに自然言語で要求（例: 'トリガーワードを@Bobに変更'）
2. Claude Codeがコードを直接編集
3. ユーザーは変更内容をgit diffで確認
4. 必要ならロールバックまたは再調整
5. `/customize`コマンドでガイド付き変更も可能

### 入力

- ユーザーの自然言語要求
- 小規模で理解可能なコードベース

### 出力

- 直接編集されたソースコード
- git diffで追跡可能な変更履歴

## 使うツール・ライブラリ

- Claude Code CLI

## コード例

```
// 設定ファイルの代わりにコード直接編集
// 例: src/index.ts 内のトリガーワード定数を変更
```

## 前提知識

- Claude Codeの基本的な使い方（スキル実行、自然言語でのコード変更依頼）
- Dockerまたはコンテナ技術の基礎知識（なぜファイルシステム分離がセキュリティに有効か）
- Node.js基礎（このプロジェクトはNode.js 20+で実装）
- Claude Agent SDKの概要（Anthropic公式のAgent実行ハーネス）
- フォーク＆ブランチベースのGitワークフロー

## 根拠

> NanoClaw provides that same core functionality, but in a codebase small enough to understand: one process and a handful of files. Claude agents run in their own Linux containers with filesystem isolation, not merely behind permission checks.

> Skills over features. Instead of adding features (e.g. support for Telegram) to the codebase, contributors submit claude code skills like /add-telegram that transform your fork.

> AI-native: No installation wizard; Claude Code guides setup. No monitoring dashboard; ask Claude what's happening. No debugging tools; describe the problem and Claude fixes it.
