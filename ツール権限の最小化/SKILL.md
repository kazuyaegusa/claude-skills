# ツール権限の最小化

> 各エージェントに必要最小限のClaude Code組み込みツールのみを許可し、不要な権限を与えない

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

レビュー専用エージェントにWriteツールを与えると誤って変更される危険がある。権限を最小化することでセキュリティとエージェントの役割境界を明確にできる

## いつ使うのか

エージェントの役割に応じた適切な権限設計をする時

## やり方

1. 読み取り専用エージェント（レビュアー、監査者）：`Read, Grep, Glob`のみ
2. 調査エージェント：`Read, Grep, Glob, WebFetch, WebSearch`
3. コード作成エージェント：`Read, Write, Edit, Bash, Glob, Grep`
4. ドキュメント作成エージェント：`Read, Write, Edit, Glob, Grep, WebFetch, WebSearch`
5. MCPサーバーや外部ツールを追加する場合は`tools`フィールドに明示的に記載

### 入力

- エージェントの役割定義

### 出力

- 必要最小限のツールセットを持つエージェント

## 使うツール・ライブラリ

- Claude Code built-in tools (Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch)

## コード例

```
# レビュー専用（変更不可）
---
name: code-reviewer
tools: Read, Grep, Glob
---

# コード生成（実行可能）
---
name: backend-developer
tools: Read, Write, Edit, Bash, Glob, Grep
---
```

## 前提知識

- Claude Code CLIがインストールされている
- claude plugin機能の基本的な理解
- サブエージェントの概念（独立したコンテキストウィンドウ、ドメイン特化型プロンプト）
- Markdown/YAMLの基本文法
