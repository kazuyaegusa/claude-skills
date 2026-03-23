# ツール権限の最小化によるセキュリティ確保

> 各サブエージェントの`tools`フィールドに、そのエージェントが実行可能なClaude Code組み込みツール（Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch等）を明示的に列挙し、不要な権限を与えない

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

レビュー専用エージェントに書き込み権限を与えない、リサーチ専用エージェントにBash実行権限を与えない等、最小権限の原則を守ることで、意図しないコード変更やシステム操作を防ぎ、安全性を高める

## いつ使うのか

セキュリティが重要なプロジェクト、複数の外部協力者が同じエージェントを使う場合、監査やレビュー専用エージェントで意図しない変更を防ぎたい場合

## やり方

1. サブエージェント定義ファイルのYAMLフロントマター`tools`フィールドを確認
2. エージェントの役割に応じて必要最小限のツールだけをカンマ区切りで列挙
3. 読み取り専用エージェント（reviewers, auditors）: `Read, Grep, Glob`
4. リサーチエージェント: `Read, Grep, Glob, WebFetch, WebSearch`
5. コード作成エージェント: `Read, Write, Edit, Bash, Glob, Grep`
6. ドキュメント作成エージェント: `Read, Write, Edit, Glob, Grep, WebFetch, WebSearch`
7. 必要に応じてMCPサーバーや外部ツールを`tools`に追加してエージェントを拡張

### 入力

- エージェントの役割定義（読み取り専用、書き込み可、実行可等）
- 利用可能なツール一覧

### 出力

- 最小権限で動作するサブエージェント設定
- 意図しない変更やリスクの低減

## 使うツール・ライブラリ

- Claude Code組み込みツール（Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch）
- MCP（Model Context Protocol）サーバー（オプション）

## コード例

```
---
name: code-reviewer
description: Code quality guardian
tools: Read, Grep, Glob  # 読み取り専用、書き込み権限なし
model: sonnet
---

---
name: backend-developer
description: Server-side expert for scalable APIs
tools: Read, Write, Edit, Bash, Glob, Grep  # フル権限
model: sonnet
---
```

## 前提知識

- Claude Code CLI がインストールされていること
- Claude Codeの基本操作（エージェント起動、ツール実行）の理解
- YAMLフロントマターの基本構文知識（エージェントカスタマイズ時）
- gitの基本操作（リポジトリクローン、ファイルコピー）
- 対象プロジェクトの技術スタックと開発フローの把握

## 根拠

> 「Tool Assignment Philosophy: Read-only agents (reviewers, auditors): Read, Grep, Glob - analyze without modifying」
