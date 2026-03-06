---
title: Multi-Agent Systems
category: architecture
tags: [agent, parallel-processing, distributed-systems, async]
dependencies: [python3.9+]
---

# Multi-Agent Systems

複数AIエージェントを並列実行し、タスクを効率的に分散処理する2つのアーキテクチャパターン。

## パターン

### 1. スター型（Star Pattern）
- 親エージェントが中心となり子エージェントを制御
- 親が全体調整と結果統合を担当
- シンプルで予測可能な処理フロー

### 2. 分散型（Distributed Pattern）  
- エージェント間で直接メッセージング
- 共有タスクリストによる自律的連携
- 動的な負荷分散で柔軟性が高い

## 使用方法

```bash
# デモ実行
python ~/.claude/skills/multi-agent-systems/demo.py

# コード内で利用
from multi_agent import StarPatternExecutor, DistributedExecutor

# スター型
executor = StarPatternExecutor()
results = await executor.execute(tasks, num_agents=3)

# 分散型
executor = DistributedExecutor()
results = await executor.execute(tasks, capabilities_map)
```

## 主要コンポーネント

- `BaseAgent`: エージェント基底クラス
- `ParentAgent/ChildAgent`: スター型実装
- `TeamAgent/TaskList`: 分散型実装
- `AgentExecutor`: 実行制御

## パフォーマンス特性

- **スター型**: 集中管理で通信オーバーヘッド小
- **分散型**: 負荷分散で処理効率高

## ユースケース

- データ処理パイプライン
- 並列APIコール
- マルチステップタスクの分散実行
- リアルタイム協調処理