# ツール権限をsubagent役割に応じて制限する

> YAML frontmatterの`tools`フィールドで、各subagentが使用できるClaude Code組み込みツールを明示的に指定する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

レビュー専門エージェントには読み取り専用権限、開発エージェントには書き込み権限を与えることで、誤った変更や意図しない実行を防ぎ、セキュリティとタスクの明確性を向上できる

## いつ使うのか

subagentの新規作成時、セキュリティ要件が厳しいタスク時、読み取り専用の分析エージェントを作成する時

## やり方

1. 読み取り専用エージェント（reviewers, auditors）に`tools: Read, Grep, Glob`を設定
2. リサーチエージェント（analysts, researchers）に`tools: Read, Grep, Glob, WebFetch, WebSearch`を追加
3. コード作成エージェント（developers, engineers）に`tools: Read, Write, Edit, Bash, Glob, Grep`を設定
4. ドキュメントエージェントに`tools: Read, Write, Edit, Glob, Grep, WebFetch, WebSearch`を設定
5. MCP serverや外部ツールを追加する場合は`tools`フィールドに明示

### 入力

- subagentの役割（読み取り専用、リサーチ、開発、ドキュメント）
- 必要な権限範囲

### 出力

- 最小権限原則に基づくsubagent設定
- 誤操作リスクの低減

## 使うツール・ライブラリ

- Claude Code built-in tools (Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch)

## コード例

```
# 読み取り専用のコードレビュアー
---
name: code-reviewer
tools: Read, Grep, Glob
---

# 調査と実装を行う開発者
---
name: backend-developer
tools: Read, Write, Edit, Bash, Glob, Grep
---

# リサーチ付きドキュメント作成者
---
name: documentation-engineer
tools: Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---
```

## 前提知識

- Claude Codeの基本的な使用経験
- subagentの概念理解（独立したコンテキストを持つ専門AIアシスタント）
- YAML frontmatterの基本構文
- コマンドラインツール（curl, git）の基本操作
- 対象言語・フレームワークの基礎知識（各subagent活用時）

## 根拠

> 「Read-only agents (reviewers, auditors): Read, Grep, Glob - analyze without modifying」「Code writers (developers, engineers): Read, Write, Edit, Bash, Glob, Grep - create and execute」
