# Progressive Disclosure でスキルを軽量化する

> スキルのメタデータ（name, description）を先にスキャンし、関連性が高い場合のみ本文とリソースをロードする3段階読み込みを実装する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

全スキルの全内容を常時読み込むと文脈窓を圧迫し、複数スキルの同時利用が不可能になるため。メタデータのみなら~100トークン、本文は<5k、リソースは必要時のみで済む

## いつ使うのか

複数のスキルをインストールしており、タスクごとに必要なスキルが変わる場合

## やり方

1. SKILL.md 冒頭に YAML frontmatter で `name` と `description` を定義
2. description は簡潔に（スキル発見用）
3. 本文に詳細な指示・例・使用方法を記述
4. scripts/ や resources/ に実行ファイル・補助資料を配置
5. Claudeは会話文脈からメタデータをスキャンし、関連度が高いスキルのみ本文をロード

### 入力

- SKILL.md（YAMLフロントマター + Markdown本文）
- オプション: scripts/, resources/ ディレクトリ

### 出力

- ~100トークンのメタデータスキャン結果
- 関連スキルの本文（<5k トークン）
- 必要時のみロードされる実行スクリプト

## 使うツール・ライブラリ

- Claude.ai Web / Claude Code CLI / Claude API

## コード例

```
---
name: my-skill
description: Brief description for skill discovery
---

# Detailed Instructions

Claude will read these when activated.

## Usage
...
```

## 前提知識

- Claude Pro, Max, Team, または Enterprise サブスクリプション（Free tier ではスキル利用不可）
- Claude.ai Web / Claude Code CLI / Claude API のいずれかへのアクセス
- YAMLとMarkdownの基本構文（スキル作成時）
- git の基本操作（チーム配布時）

## 根拠

> Skills employ a **progressive disclosure architecture** for efficiency: 1. **Metadata loading** (~100 tokens): Claude scans available Skills to identify relevant matches 2. **Full instructions** (<5k tokens): Load when Claude determines the Skill applies 3. **Bundled resources**: Files and executable code load only as needed
