---
title: マルチエージェントパターン解説
slug: multi-agent-patterns
description: Subagent・Multi-Agents・Agent Teamsの3パターンを体系的に理解し、適切に使い分ける
tags: [claude-code, codex, multi-agent, architecture, design-pattern]
author: AI Skill Extractor
created: 2026-03-07
updated: 2026-03-07
---

# マルチエージェントパターン解説

Claude CodeとCodexが提供する3つのマルチエージェントパターンを体系的に理解し、タスクに応じて適切に選択・実装するためのスキル。

## 概要

マルチエージェント機能の本質は「エージェント間の通信構造」にある。各パターンの違いを理解することで、タスクに最適な実装方法を選択できる。

## 3つのパターン

### 1. Subagentパターン（1対1委譲型）

**特徴**
- 親が子に特定タスクを委譲
- 子は独立したコンテキストで作業
- 完了後に結果を親に返却
- 最もシンプルで予測可能

**適用場面**
- 特定領域の専門処理が必要な場合
- タスクが明確に分離できる場合
- 依存関係がない単独タスクの場合

**Claude Codeでの実装**
```bash
claudeCode> /task "ログファイルを解析して異常を検出" subagent_type=general-purpose
```

### 2. Multi-Agentsパターン（並列実行型）

**特徴**
- 複数エージェントを並列起動
- 各エージェントは独立して動作
- 親子間での継続的なやり取り可能
- 終了タイミングを明示的に制御

**適用場面**
- 独立した複数タスクがある場合
- 処理時間を短縮したい場合
- 各タスクの結果を統合する場合

**Codexでの実装**
```python
# 複数エージェントを並列実行
agents = [
    {"name": "data_agent", "task": "データ収集"},
    {"name": "api_agent", "task": "API統合"},
    {"name": "report_agent", "task": "レポート生成"}
]
# 各エージェントが並列で動作
```

### 3. Agent Teamsパターン（分散協調型）

**特徴**
- エージェント間の直接通信
- 共有タスクリストで協調
- 依存関係を自動管理
- 複雑なワークフローに対応

**適用場面**
- タスク間に依存関係がある場合
- 段階的な処理が必要な場合
- チーム全体での最適化が必要な場合

**Claude Codeでの実装**
```bash
# Agent Teamの作成
claudeCode> /team create "feature-dev"
claudeCode> /team add-agent explore haiku "要件調査"
claudeCode> /team add-agent implement sonnet "実装" --depends-on "要件調査"
claudeCode> /team run
```

## パターン選択ガイドライン

```
タスクは独立している？
├─ YES → 並列実行可能？
│        ├─ YES → Multi-Agents
│        └─ NO → Subagent
└─ NO → 複雑な依存関係？
         ├─ YES → Agent Teams
         └─ NO → Subagent（逐次実行）
```

## 実装のベストプラクティス

### Subagent使用時
1. タスクを明確に定義する
2. 必要な情報をすべて渡す
3. 結果の形式を事前に決める

### Multi-Agents使用時
1. 各エージェントの役割を明確化
2. 並列度を適切に設定（リソース考慮）
3. 結果の統合方法を事前設計

### Agent Teams使用時
1. 依存関係を正確にマッピング
2. 適切なモデル選択（haiku/sonnet/opus）
3. エラー処理とリトライ戦略

## パフォーマンス特性

| パターン | レイテンシ | スループット | メモリ使用 | 複雑度 |
|---------|----------|------------|-----------|-------|
| Subagent | 低 | 低 | 低 | シンプル |
| Multi-Agents | 中 | 高 | 高 | 中 |
| Agent Teams | 高 | 中 | 中 | 複雑 |

## トラブルシューティング

### よくある問題と解決策

**問題**: エージェントがタイムアウトする
- 解決: タスクを細分化、タイムアウト値を調整

**問題**: 依存関係でデッドロック
- 解決: 循環依存を排除、Agent Teamsの依存グラフを確認

**問題**: メモリ不足
- 解決: 並列度を下げる、結果をストリーミング処理

## デモの実行

```bash
# パターン比較デモ
python3 ~/.claude/skills/multi-agent-patterns/demo.py
```

## 参考資料

- [Claude Code Agent Teams Documentation](https://docs.claude.com/agent-teams)
- [Codex Multi-Agents Guide](https://codex.dev/multi-agents)
- [Distributed Systems Patterns](https://martinfowler.com/articles/patterns-of-distributed-systems/)