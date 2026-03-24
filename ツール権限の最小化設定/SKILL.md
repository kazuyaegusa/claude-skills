# ツール権限の最小化設定

> 各サブエージェントの役割に応じて、アクセスできるClaude Code組み込みツール(Read, Write, Edit, Bash, Grep, Glob, WebFetch, WebSearch等)を制限する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

読み取り専用エージェント(レビュアー、監査者)が誤ってコードを書き換えたり、リサーチエージェントが不要にBash実行したりするリスクを排除するため。最小権限の原則に従い、セキュリティとエラー防止を両立する

## いつ使うのか

新規サブエージェントを作成する時、または既存エージェントのセキュリティポリシーを強化したい時

## やり方

1. エージェント定義ファイルのfrontmatterで `tools:` フィールドに許可するツールをカンマ区切りで列挙
2. **読み取り専用エージェント**(code-reviewer, security-auditor等): `tools: Read, Grep, Glob`
3. **リサーチエージェント**(research-analyst, competitive-analyst等): `tools: Read, Grep, Glob, WebFetch, WebSearch`
4. **コード生成エージェント**(python-pro, backend-developer等): `tools: Read, Write, Edit, Bash, Glob, Grep`
5. **ドキュメントエージェント**(documentation-engineer, technical-writer等): `tools: Read, Write, Edit, Glob, Grep, WebFetch, WebSearch`
6. MCP ServerやExternal Toolsを追加したい場合は `tools:` に明示的に追加
7. 全ツールを継承したい場合は `tools:` を空欄にする

### 入力

- エージェントの責務(読み取り専用/書き込み可能/外部情報取得の要否)
- 必要な最小限のツールセット

### 出力

- frontmatter内の `tools:` フィールド
- 実行時のツールアクセス制限

## 使うツール・ライブラリ

- Claude Code tool permission system

## コード例

```
---
name: code-reviewer
description: Code quality guardian
tools: Read, Grep, Glob
model: sonnet
---

---
name: backend-developer
description: Server-side expert for scalable APIs
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---
```

## 前提知識

- Claude Code CLIの基本操作(/agents コマンド、サブエージェント概念)
- Markdownの読み書き(frontmatterとYAML構文)
- Bashコマンド(curl, chmod)の基礎知識
- プロジェクトとグローバルの設定ファイル配置の違い(~/.config vs .config的な概念)
- 開発ライフサイクル(開発→テスト→デプロイ→運用)の理解
