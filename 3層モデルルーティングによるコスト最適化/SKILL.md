# 3層モデルルーティングによるコスト最適化

> タスク複雑度を自動判定し、Tier 1（Agent Booster、$0）→Tier 2（Haiku、$0.0002）→Tier 3（Opus、$0.015）の最安モデルに振り分け

- 出典: https://github.com/ruvnet/ruflo
- 投稿者: ruvnet
- カテゴリ: agent-orchestration

## なぜ使うのか

すべてのタスクにOpusを使うと無駄が多い。複雑度に応じて最小コストで要件を満たすモデルを選ぶことで、APIコストを75%削減しつつClaude Max利用量を2.5倍拡張できる

## いつ使うのか

日常的な開発作業（ドキュメント修正、簡単なバグ修正、リファクタリング）でコストを抑えたい場合

## やり方

1. `hooks pre-task`でタスクをキーワード・構文解析
2. 複雑度スコア算出（<30%=Low、30-70%=Medium、>70%=High）
3. Low→Agent Booster（LLMスキップ）、Medium→Haiku/Sonnet、High→Opusに自動ルーティング
4. `[TASK_MODEL_RECOMMENDATION] Use model="haiku"`シグナルで推奨モデル表示
5. Task toolに`model: "haiku"`パラメータを渡して実行

### 入力

- タスク記述文
- （オプション）コスト優先フラグ

### 出力

- 推奨モデル（haiku/sonnet/opus）
- 複雑度スコア
- 推定コスト

## 使うツール・ライブラリ

- @claude-flow/router（ModelRouter）
- @claude-flow/hooks（複雑度判定）

## コード例

```
const router = new ModelRouter();
const result = await router.route({ task: 'Add console.log to function', preferCost: true });
// Returns: { model: 'haiku', reason: 'simple task, low complexity' }
// コスト節約: 75%削減、Claude Max利用量: 2.5倍拡張
```

## 前提知識

- Node.js 20+とnpm 9+
- Claude Code CLIのインストール（`npm install -g @anthropic-ai/claude-code`）
- Anthropic APIキー（Claude利用時）またはClaude Codeサブスクリプション
- 基本的なTypeScript/JavaScriptの知識
- （オプション）Docker（RuVector PostgreSQL利用時）
- （オプション）Git、GitHub CLI（GitHub統合時）
- マルチエージェントシステムの基本概念理解（推奨）
