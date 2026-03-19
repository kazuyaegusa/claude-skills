# Skills と MCP を使い分ける

> 再利用可能なタスク手順は Skills、外部データ・API統合は MCP として実装し、必要に応じて組み合わせる

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

Skills は手順的知識の移植性が高く、MCP は外部システムへのリアルタイムアクセスに特化しているため。Skills で MCP サーバーを構築するスキル（mcp-builder）も存在

## いつ使うのか

外部データソース（GitHub API, Notion, PostgreSQL 等）と連携しつつ、定型ワークフローも再利用したい場合

## やり方

1. タスクが「何度も同じ手順を踏む」なら Skills を作成
2. 外部DB・API・ファイルシステムへのアクセスが必要なら MCP サーバーを構築
3. Skills から MCP ツールを呼び出す形で統合
4. mcp-builder スキルを使って高品質な MCP サーバーを生成

### 入力

- Skills: SKILL.md + scripts/
- MCP: サーバー設定 + ツール定義

### 出力

- Skills: 移植可能なタスク手順
- MCP: 外部データアクセスツール

## 使うツール・ライブラリ

- Claude Skills（SKILL.md）
- Model Context Protocol（MCP server）
- mcp-builder スキル

## コード例

```
# Skills: Reusable procedural knowledge
# MCP: External data/API integration
# Use mcp-builder skill to create MCP servers
```

## 前提知識

- Claude Pro, Max, Team, または Enterprise サブスクリプション（Free tier ではスキル利用不可）
- Claude.ai Web / Claude Code CLI / Claude API のいずれかへのアクセス
- YAMLとMarkdownの基本構文（スキル作成時）
- git の基本操作（チーム配布時）

## 根拠

> Skills employ a **progressive disclosure architecture** for efficiency: 1. **Metadata loading** (~100 tokens): Claude scans available Skills to identify relevant matches 2. **Full instructions** (<5k tokens): Load when Claude determines the Skill applies 3. **Bundled resources**: Files and executable code load only as needed

> **Use Skills when**: Capabilities should be accessible to any Claude instance. They're portable expertise.

> ⚠️ **Important**: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.

> **Skills** | Reusable procedural knowledge across conversations | Same format everywhere (Claude.ai, Code, API) | Can include executable scripts | 30-50 tokens until loaded

> **MCP** | External data/API integration | Requires server configuration | Provides tools/resources | Varies by implementation
