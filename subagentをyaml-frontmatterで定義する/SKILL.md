# subagentをYAML frontmatterで定義する

> マークダウンファイルの先頭にname/description/tools/modelをYAMLブロックで記述し、本文に役割・チェックリスト・通信プロトコルを書く

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

専門性（役割定義）、ツール権限（セキュリティ）、モデル選択（コスト最適化）を1ファイルにまとめることで、再利用と配布が容易になり、チーム全体で統一された動作を保証できる

## いつ使うのか

新しい専門タスク用のsubagentを作成・共有する時、既存エージェントの権限やモデルを調整する時

## やり方

1. `---`で囲んだYAMLブロックに`name`, `description`, `tools`, `model`を記述
2. 本文に「You are a [role]...」で専門性を定義
3. チェックリスト、ワークフロー、コミュニケーションプロトコルを構造化して記述
4. `.claude/agents/`（プロジェクト固有）または`~/.claude/agents/`（グローバル）に配置

### 入力

- 役割の明確な定義（例: TypeScript専門家、セキュリティ監査担当）
- 必要なツールのリスト（Read, Write, Edit, Bash, Glob, Grep, WebFetch等）
- 使用するモデル（opus/sonnet/haiku/inherit）

### 出力

- 独立したコンテキストで動作する専門subagent
- チーム全体で再利用可能な`.md`ファイル

## 使うツール・ライブラリ

- Claude Code subagent機能
- YAML frontmatter

## コード例

```
---
name: typescript-pro
description: TypeScript specialist for type safety and modern patterns
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---

You are a TypeScript expert specializing in type-safe code and modern patterns...

## Development Workflow
1. Analyze type definitions
2. Implement with strict mode
3. Validate with tsc --noEmit
```

## 前提知識

- Claude Codeの基本的な使用経験
- subagentの概念理解（独立したコンテキストを持つ専門AIアシスタント）
- YAML frontmatterの基本構文
- コマンドラインツール（curl, git）の基本操作
- 対象言語・フレームワークの基礎知識（各subagent活用時）

## 根拠

> 「Domain-Specific Intelligence: Subagents come equipped with carefully crafted instructions tailored to their area of expertise」
