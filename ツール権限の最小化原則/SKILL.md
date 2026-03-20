# ツール権限の最小化原則

> サブエージェントごとに必要最小限のClaude Codeツール（Read, Write, Edit, Bash等）のみを許可し、不要な権限を与えない

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

全ツールアクセスを許可すると、レビュー専用エージェントが誤ってコードを書き換えたり、研究エージェントが本番環境でBashコマンドを実行するリスクがあるため

## いつ使うのか

セキュリティリスクを低減しつつ、エージェントの役割を明確化したい場合

## やり方

1. レビュー・監査エージェントには `tools: Read, Grep, Glob` のみを設定
2. リサーチエージェントには `tools: Read, Grep, Glob, WebFetch, WebSearch` を設定
3. コード実装エージェントには `tools: Read, Write, Edit, Bash, Glob, Grep` を設定
4. ドキュメント生成エージェントには `tools: Read, Write, Edit, Glob, Grep, WebFetch, WebSearch` を設定
5. YAML frontmatterの `tools` フィールドを編集して適用

### 入力

- エージェントの役割定義（レビュー/実装/研究/ドキュメント等）
- 利用可能なClaude Codeツールのリスト

### 出力

- 最小権限で動作するサブエージェント
- 誤操作リスクの低減

## 使うツール・ライブラリ

- Claude Code（ツール権限管理機能）

## コード例

```
---
name: code-reviewer
tools: Read, Grep, Glob  # 読み取りのみ、書き込み禁止
---

---
name: backend-developer
tools: Read, Write, Edit, Bash, Glob, Grep  # フルアクセス
---
```

## 前提知識

- Claude Codeの基本操作（CLI起動、エージェント呼び出し）
- サブエージェントの概念理解（独立コンテキスト、ツール権限、モデル選択）
- YAML frontmatter形式の基本構造
- Git操作（クローン、ファイルコピー）またはcurlコマンドの使用
- 対象領域（言語・インフラ・QA等）の基礎知識（各エージェントを活用する場合）

## 根拠

> 「Tool Assignment Philosophy: Each subagent's `tools` field specifies Claude Code built-in tools, optimized for their role」
