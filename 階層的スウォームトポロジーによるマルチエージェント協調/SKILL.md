# 階層的スウォームトポロジーによるマルチエージェント協調

> クイーンエージェントが戦略を決定し、ワーカーエージェント（researcher, coder, tester等）に作業を分配、Byzantine耐障害性コンセンサスで合意形成する

- 出典: https://github.com/ruvnet/ruflo
- 投稿者: ruvnet
- カテゴリ: agent-orchestration

## なぜ使うのか

単一エージェントでは複雑タスクの分解・並行処理が困難。複数エージェントが協調することで、各自の専門性を活かし、全体としての生産性が2.8-4.4倍向上する

## いつ使うのか

6つ以上のステップが必要な複雑タスク、または複数ドメイン（セキュリティ+パフォーマンス+テスト）にまたがるタスク

## やり方

1. `npx ruflo hive-mind init`でクイーンとワーカーを初期化
2. `npx ruflo hive-mind spawn "Build API" --queen-type tactical --consensus byzantine`でスウォーム起動
3. クイーンがタスクを分解し、ワーカーに割り当て
4. Byzantine投票（2/3多数決）で各決定を承認
5. 共有メモリ（collective memory）で知識を同期

### 入力

- タスク記述（例: "ユーザー認証機能の実装"）
- クイーンタイプ（strategic/tactical/adaptive）
- コンセンサスアルゴリズム（majority/weighted/byzantine）

### 出力

- 各ワーカーの実行結果
- コンセンサスログ（どの決定が承認されたか）
- collective memoryに蓄積された知識

## 使うツール・ライブラリ

- @claude-flow/swarm（スウォーム管理）
- @claude-flow/memory（AgentDB、共有メモリ）
- Byzantine/Raft/Gossipコンセンサスプロトコル

## コード例

```
const swarm = await createSwarm({ topology: 'hierarchical', maxAgents: 8, strategy: 'specialized' });
await swarm.spawn('coder', { name: 'coder-1' });
await swarm.spawn('tester', { name: 'tester-1' });
const result = await swarm.orchestrate({ task: 'Implement user auth', strategy: 'adaptive' });
```

## 前提知識

- Node.js 20+とnpm 9+
- Claude Code CLIのインストール（`npm install -g @anthropic-ai/claude-code`）
- Anthropic APIキー（Claude利用時）またはClaude Codeサブスクリプション
- 基本的なTypeScript/JavaScriptの知識
- （オプション）Docker（RuVector PostgreSQL利用時）
- （オプション）Git、GitHub CLI（GitHub統合時）
- マルチエージェントシステムの基本概念理解（推奨）
