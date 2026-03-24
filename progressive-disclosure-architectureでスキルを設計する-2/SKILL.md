# Progressive Disclosure Architectureでスキルを設計する

> メタデータ（100トークン）→本体（<5k）→リソース（オンデマンド）の3段階でコンテンツを開示し、コンテキストウィンドウを節約しながら多数のスキルを利用可能にする

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

常時全スキルをロードするとトークン消費が膨大になる。関連性判定→詳細ロード→必要リソースのみ取得という段階を踏むことで、複数スキルを同時利用可能かつ効率的な運用が実現できる

## いつ使うのか

複数のスキルを同時利用可能にしたいとき、トークン効率を最大化したいとき

## やり方

1. SKILL.mdのfrontmatterに`name`と簡潔な`description`を記載（メタデータスキャン用）
2. 本体に詳細な手順・例を記載（5k未満に抑える）
3. scripts/やresources/フォルダに実行可能スクリプトや補助ファイルを配置（必要時のみロード）
4. Claudeが自動でメタデータスキャン→関連スキル判定→本体ロード→リソース実行の流れを制御

### 入力

- スキル名
- 簡潔な説明文
- 詳細手順
- オプショナルなスクリプト/リソース

### 出力

- 段階的にロードされる効率的なスキル構造

## 使うツール・ライブラリ

- YAML frontmatter
- Markdown
- Python/JavaScript等の実行可能スクリプト

## コード例

```
---
name: my-skill
description: Brief description for skill discovery
---

# Detailed Instructions
Claude reads these when activated...

## Usage
...

scripts/helper.py, resources/template.json など必要時のみロード
```

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（Freeプランではスキル利用不可）
- YAML frontmatter、Markdown記法の基礎知識
- Git/GitHubの基本操作（バージョン管理・配布時）
- Python/JavaScriptなどスクリプト言語の基礎（カスタムスキル作成時）
- Claude Code CLI、Claude.ai、またはClaude APIの利用経験
- プロンプトエンジニアリング、MCP、Subagents、Projectsとの違いの理解

## 根拠

> Skills employ a **progressive disclosure architecture** for efficiency: 1. Metadata loading (~100 tokens) 2. Full instructions (<5k tokens) 3. Bundled resources

> **Nov 13, 2025**: Anthropic publishes Skills Explained - Comprehensive guide covering progressive disclosure architecture, decision matrices
