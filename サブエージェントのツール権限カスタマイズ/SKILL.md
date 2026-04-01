# サブエージェントのツール権限カスタマイズ

> 各サブエージェントのfrontmatter `tools:` フィールドを編集し、アクセス可能なClaude Code組み込みツールを制限または拡張する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

セキュリティ制御（レビュー専用エージェントには書き込み権限を与えない）、タスク特化（リサーチエージェントにはWebFetch/WebSearchのみ）、誤操作防止のため

## いつ使うのか

監査・レビュー専用エージェント（読み取り専用）、リサーチエージェント（検索+読み取り）、開発エージェント（全権限）のように役割別に権限を分離したい時

## やり方

1. サブエージェント.mdファイルのfrontmatter（YAMLヘッダ）を開く
2. `tools:` 行を編集（例: `tools: Read, Grep, Glob` で読み取り専用に制限、`tools: Read, Write, Edit, Bash, Glob, Grep` で開発者権限）
3. 必要に応じてMCPサーバーや外部ツールを追加
4. 保存後、次回呼び出し時に新しい権限が適用される

### 入力

- サブエージェント定義ファイル（.md）への書き込み権限
- Claude Code組み込みツール一覧の理解

### 出力

- カスタマイズされた権限セットを持つサブエージェント

## 使うツール・ライブラリ

- テキストエディタ
- Claude Code

## コード例

```
---
name: security-auditor
tools: Read, Grep, Glob
model: opus
---
```

## 前提知識

- Claude Codeがインストール・セットアップ済み
- サブエージェントの概念理解（独立したコンテキストウィンドウ、ドメイン特化プロンプト、ツール権限管理）
- 基本的なCLI操作（curl, chmod, git clone等）
- YAMLフロントマター形式の理解（サブエージェント定義ファイルの編集時）
- Claude Codeの /agents コマンドとサブエージェント呼び出し構文の理解

## 根拠

> "Read-only agents (reviewers, auditors): `Read, Grep, Glob` - analyze without modifying"

> "Code writers (developers, engineers): `Read, Write, Edit, Bash, Glob, Grep` - create and execute"
