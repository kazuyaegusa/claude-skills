# SKILL.md形式でエージェント用知識を構造化

> フロントマター + 指示・ワークフロー・意思決定フレームワークをMarkdownで定義し、AIエージェントが解釈可能な形で専門知識をパッケージ化する

- 出典: https://github.com/alirezarezvani/claude-skills
- 投稿者: alirezarezvani
- カテゴリ: claude-code-workflow

## なぜ使うのか

自然言語による柔軟な知識記述と、構造化による機械的な処理の両立が可能になる。また、複数ツール間での知識の移植性が高まる

## いつ使うのか

AIエージェントに新しい専門領域の知識を追加したい時、または既存の暗黙知を明示的なスキルとして定型化したい時

## やり方

1. スキルフォルダ内に SKILL.md を配置
2. フロントマター部分にメタデータ（スキル名、説明、カテゴリ等）を記述
3. 本文に具体的な指示、ワークフロー、チェックリスト、意思決定基準を記述
4. 必要に応じて scripts/, references/, assets/ を追加
5. ~/.claude/skills/ や ~/.codex/skills/ に配置

### 入力

- 専門領域の知識（アーキテクチャ原則、規制要件、マーケティング手法等）
- 対象となるタスクの典型的なワークフロー

### 出力

- SKILL.md ファイル
- （オプション）実行可能なPythonスクリプト群
- 参照ドキュメント・テンプレート

## 使うツール・ライブラリ

- Markdown
- Python標準ライブラリ（スクリプト用）

## コード例

```
# SKILL.md の例（フロントマター部分）
---
name: security-auditor
description: Scan codebases for security vulnerabilities
category: engineering
tier: powerful
---

# Instructions
1. Scan for hardcoded secrets
2. Check dependency vulnerabilities
3. Analyze authentication flows
...
```

## 前提知識

- Claude CodeまたはOpenAI Codex等のAIコーディングツールの基本的な使い方
- SKILL.md形式やエージェント概念の理解（ただしREADMEに説明あり）
- Bash/シェルスクリプトの基本知識（インストールスクリプト実行用）
- Python 3.x の実行環境（CLIツール使用時）
- Git/GitHub の基本操作
