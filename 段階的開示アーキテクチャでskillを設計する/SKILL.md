# 段階的開示アーキテクチャでSkillを設計する

> Skillをメタデータ・命令・リソースの3層に分け、関連性に応じて段階的にロードすることでトークン効率を最大化する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

全Skillを常時フルロードするとコンテキストウィンドウを圧迫し、複数Skillの併用が困難になる。段階的開示により30-50トークンで待機し、必要時のみ詳細をロードできる

## いつ使うのか

複数のSkillを同時に利用可能にしたいが、トークン上限を気にする場合、または組織内で多数のSkillを配布する場合

## やり方

1. SKILL.mdの先頭にYAMLフロントマター（name, description）を記述（~100トークン）
2. 本文に詳細な命令・使用例を記載（<5kトークン）
3. scripts/とresources/ディレクトリに実行可能スクリプトやテンプレートを配置
4. Claudeはタスクに応じてdescriptionをスキャン→関連性判定→本文ロード→リソース実行の順で処理

### 入力

- Skillの目的・タスク定義
- メタデータ用の簡潔な説明文（discovery用）
- 詳細な実行手順
- （オプション）実行可能スクリプトやテンプレートファイル

### 出力

- SKILL.md（YAMLフロントマター + 本文）
- scripts/ディレクトリ（必要に応じて）
- resources/ディレクトリ（必要に応じて）

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

- Claude Pro/Max/Team/Enterpriseアカウント（無料tierはSkills非対応）
- Claude.ai Web、Claude Code CLI、またはClaude APIへのアクセス
- YAMLフロントマターの基本的な理解
- （カスタムSkill作成時）Pythonやシェルスクリプトの基礎知識
