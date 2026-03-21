# ツールベースの最小権限原則（Least Privilege）

> 各サブエージェントに必要最小限のツール権限のみを付与し、読み取り専用エージェント（レビュー、監査）とコード変更エージェント（開発、リファクタリング）を明確に分離する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

セキュリティリスクを低減し、意図しないコード変更や情報漏洩を防ぐため

## いつ使うのか

セキュアな開発環境を構築したい時、エージェントの役割を厳格に分離したい時

## やり方

1. レビュー・監査系エージェント（code-reviewer, security-auditor等）には `tools: Read, Grep, Glob` のみ指定
2. リサーチ系エージェント（research-analyst等）には `Read, Grep, Glob, WebFetch, WebSearch` を指定
3. 開発・変更系エージェント（backend-developer, refactoring-specialist等）には `Read, Write, Edit, Bash, Glob, Grep` を指定
4. ドキュメント生成エージェントには `Read, Write, Edit, Glob, Grep, WebFetch, WebSearch` を指定
5. 必要に応じてMCPサーバーや外部ツールを `tools` フィールドに追加可能

### 入力

- エージェントの役割（読み取り専用 or 変更可能）
- 必要な外部連携（Web検索、API呼び出し等）

### 出力

- 権限範囲が明確なサブエージェント定義
- 監査可能なツール使用履歴

## 使うツール・ライブラリ

- Claude Code built-in tools (Read, Write, Edit, Bash, Grep, Glob, WebFetch, WebSearch)
- MCP servers (オプション)

## コード例

```
# 読み取り専用レビューエージェント
---
name: code-reviewer
tools: Read, Grep, Glob
---

# 開発エージェント
---
name: backend-developer
tools: Read, Write, Edit, Bash, Glob, Grep
---
```

## 前提知識

- Claude Codeの基本的な使い方（サブエージェント機能の理解）
- YAMLフロントマターとMarkdownの読み書き
- コマンドラインツール（claude CLI、curl、bash）の操作経験
- 開発ドメイン知識（各サブエージェントを効果的に使うため、対象領域の基礎理解が必要）

## 根拠

> 「Read-only agents (reviewers, auditors): Read, Grep, Glob - analyze without modifying」

> 「Code writers (developers, engineers): Read, Write, Edit, Bash, Glob, Grep - create and execute」
