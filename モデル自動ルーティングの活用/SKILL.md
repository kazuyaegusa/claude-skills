# モデル自動ルーティングの活用

> サブエージェント定義のYAML `model` フィールドで、タスクの複雑度に応じてOpus/Sonnet/Haikuを指定し、コスト最適化と品質のバランスをとる

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

全タスクを最高性能モデルで実行するとコストが高く、逆に全て低性能モデルだと品質が低下するため、タスク種別に応じた自動ルーティングが必要

## いつ使うのか

LLMコストを最適化しつつ、タスクごとに適切な推論能力を確保したい場合

## やり方

1. 深い推論が必要なタスク（セキュリティ監査、アーキテクチャレビュー）には `model: opus` を設定
2. 日常的なコーディング（機能追加、リファクタリング）には `model: sonnet` を設定
3. 軽量タスク（ドキュメント生成、依存関係チェック）には `model: haiku` を設定
4. メインセッションのモデルを継承したい場合は `model: inherit` を設定
5. エージェント定義ファイルのYAMLヘッダーを編集して適用

### 入力

- サブエージェント定義ファイル（.md）
- タスクの複雑度分類（高/中/低）

### 出力

- コスト効率と品質のバランスが取れたAIアシスト
- 自動的にモデルが切り替わるエージェントセッション

## 使うツール・ライブラリ

- Claude Code（モデルルーティング機能）

## コード例

```
---
name: security-auditor
model: opus  # 深い推論が必要
---

---
name: python-pro
model: sonnet  # 日常的なコーディング
---

---
name: documentation-engineer
model: haiku  # 軽量タスク
---
```

## 前提知識

- Claude Codeの基本操作（CLI起動、エージェント呼び出し）
- サブエージェントの概念理解（独立コンテキスト、ツール権限、モデル選択）
- YAML frontmatter形式の基本構造
- Git操作（クローン、ファイルコピー）またはcurlコマンドの使用
- 対象領域（言語・インフラ・QA等）の基礎知識（各エージェントを活用する場合）

## 根拠

> 「Smart Model Routing: Each subagent includes a `model` field that automatically routes it to the right Claude model — balancing quality and cost」
