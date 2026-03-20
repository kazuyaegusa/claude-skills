# Progressive Disclosure Architectureでスキルを設計する

> スキルのメタデータ（name/description）を軽量に保ち、詳細な指示とリソースは必要時のみ読み込む3段階構造でスキルを構成する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

複数スキルを同時に利用可能な状態にしながら、Claudeのコンテキストウィンドウを浪費しないため。メタデータスキャン（~100トークン）→本文読込（<5kトークン）→リソース読込の順で段階的に開示する。

## いつ使うのか

再利用可能なワークフローや手順をスキルとして定義する全ての場面

## やり方

1. SKILL.mdのYAMLフロントマター（name/description）を簡潔に記述（スキル発見用）
2. SKILL.md本文に詳細な指示を記載（スキル起動時に読まれる）
3. scripts/やresources/ディレクトリに実行可能コードや補助ファイルを配置（必要時のみ参照）
4. descriptionは「スキル発見」のためのもので、詳細はSKILL.md本文に書く

### 入力

- 再利用したいワークフローの手順
- スキルの目的を表すname（識別子）
- スキル発見用の簡潔なdescription

### 出力

- メタデータ（~100トークン）
- 詳細指示（<5kトークン）
- 必要時のみ読まれるリソース

## 使うツール・ライブラリ

- YAML frontmatter
- Markdown

## コード例

```
---
name: my-skill
description: Brief description for skill discovery (keep concise)
---

# Detailed Instructions

Claude will read these instructions when the skill is activated.

## Usage
Explain how to use this skill...

## Examples
Provide clear examples...
```

## 前提知識

- Claude.ai Pro/Max/Team/Enterpriseアカウント（Freeユーザーはスキル利用不可）
- YAML frontmatter、Markdownの基本知識
- （API利用の場合）Anthropic APIキーとAPI仕様の理解
- （Claude Code利用の場合）Claude Code CLIのインストール

## 根拠

> Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens) 2. Full instructions (<5k tokens) 3. Bundled resources

> Q: How much do skills impact token usage? A: Skills are highly efficient thanks to progressive disclosure. Each skill uses only ~100 tokens during metadata scanning to determine relevance.
