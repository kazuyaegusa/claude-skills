# モデルルーティングによるコスト最適化

> タスクの複雑度に応じて、opus（高度推論）、sonnet（日常コーディング）、haiku（軽量タスク）を自動選択する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

全てのタスクでopusを使うとコストが膨らむが、適切にモデルを使い分けることで品質を保ちつつコストを削減できる

## いつ使うのか

大規模チームで多数のサブエージェントを運用する時、コストと品質のバランスを最適化したい時

## やり方

1. 深い推論が必要なタスク（アーキテクチャレビュー、セキュリティ監査、金融ロジック）には `model: opus` を指定
2. 通常のコーディング（書き込み、デバッグ、リファクタリング）には `model: sonnet` を指定
3. 軽量タスク（ドキュメント生成、検索、依存関係チェック）には `model: haiku` を指定
4. メイン会話のモデルを継承したい場合は `model: inherit` を指定
5. フロントマターの `model` フィールドを編集することで、いつでも変更可能

### 入力

- タスクの性質（推論深度、コード変更の複雑度等）

### 出力

- コスト効率の高いエージェント構成
- 品質を犠牲にしない開発速度

## 使うツール・ライブラリ

- Claude Opus
- Claude Sonnet
- Claude Haiku

## コード例

```
# 高度推論が必要な監査エージェント
---
name: security-auditor
model: opus
---

# 日常的なコーディング
---
name: python-pro
model: sonnet
---

# 軽量なドキュメント生成
---
name: documentation-engineer
model: haiku
---
```

## 前提知識

- Claude Codeの基本的な使い方（サブエージェント機能の理解）
- YAMLフロントマターとMarkdownの読み書き
- コマンドラインツール（claude CLI、curl、bash）の操作経験
- 開発ドメイン知識（各サブエージェントを効果的に使うため、対象領域の基礎理解が必要）
