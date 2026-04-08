# subagent-catalogスキルの提供

> Claude Code内から `/subagent-catalog:search <query>` でagentを検索・取得できるスキルを提供

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

GitHubを離れずにClaude Code内で完結すれば、開発フローが中断されない。キーワード検索・カテゴリ一覧・agent定義の即座取得により、必要なagentを数秒で導入できる

## いつ使うのか

Claude Code内で効率的にagentを探したいとき

## やり方

1. tools/subagent-catalog/を~/.claude/commands/にコピー
2. `/subagent-catalog:search <query>` で名前・説明・カテゴリから検索
3. `/subagent-catalog:fetch <name>` でagent定義全文を取得
4. `/subagent-catalog:list` で全カテゴリを一覧表示
5. `/subagent-catalog:invalidate` でキャッシュを更新

### 入力

- 検索クエリ（agent名・キーワード）

### 出力

- マッチしたagentのリストまたは定義全文

## 使うツール・ライブラリ

- Claude Code slash commands

## コード例

```
# インストール
cp -r tools/subagent-catalog ~/.claude/commands/

# 使用例
/subagent-catalog:search python
/subagent-catalog:fetch python-pro
/subagent-catalog:list
```

## 前提知識

- Claude Codeの基本操作（subagent作成・呼び出し）
- YAML frontmatterの理解
- Claude APIのモデル種別（opus/sonnet/haiku）の特性
- ~/.claude/agents/ と .claude/agents/ の違い（global/project-specific）
- 最小権限の原則（Principle of Least Privilege）

## 根拠

> This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.

> 4 installation methods: Plugin (claude plugin install), Manual, Interactive installer (./install-agents.sh), Agent installer (via Claude Code)
