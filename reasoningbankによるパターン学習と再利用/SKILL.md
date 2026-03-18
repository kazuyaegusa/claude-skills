# ReasoningBankによるパターン学習と再利用

> 成功したタスク実行の軌跡（trajectory）をHNSW索引付きベクトルストアに保存し、類似タスクで過去のパターンを0.1ms未満で検索・適用する

- 出典: https://github.com/ruvnet/ruflo
- 投稿者: ruvnet
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントは毎回ゼロから考えるのではなく、過去の成功例を学習することで、検出精度が50-60%→90.5%に向上し、初回からベストプラクティスを適用できる

## いつ使うのか

繰り返し発生するタスク（認証実装、API設計、セキュリティ監査等）で、過去の知見を活かしたい場合

## やり方

1. タスク開始時に`hooks route "<task>"`で類似パターンを検索（HNSW、150x高速）
2. 上位5件のパターンをコンテキストに注入
3. タスク実行後、`hooks post-task --success true`で成功軌跡を記録
4. JUDGE（成功/失敗判定）→DISTILL（キー学習の抽出、LoRA）→CONSOLIDATE（EWC++で忘却防止）のパイプライン実行
5. 次回以降、同種タスクで自動的にこのパターンが優先される

### 入力

- タスククエリ（例: "JWT認証の実装"）
- 成功/失敗フラグ
- 品質スコア（0.0-1.0）

### 出力

- 類似パターン一覧（similarity score付き）
- 推奨エージェント（例: security-architect、94%信頼度）
- 学習後の更新されたパターンDB

## 使うツール・ライブラリ

- @claude-flow/hooks（ReasoningBank統合）
- @claude-flow/memory（HNSW索引、AgentDB）
- ONNX Runtime（ローカル埋め込み生成、75x高速）

## コード例

```
const bank = new ReasoningBank();
await bank.recordOutcome({ task: 'implement authentication', outcome: 'JWT with refresh tokens', success: true });
const patterns = await bank.retrieveSimilar('add user login', { k: 5 });
await bank.distill(); // LoRAでキー学習抽出
await bank.consolidate(); // EWC++で忘却防止
```

## 前提知識

- Node.js 20+とnpm 9+
- Claude Code CLIのインストール（`npm install -g @anthropic-ai/claude-code`）
- Anthropic APIキー（Claude利用時）またはClaude Codeサブスクリプション
- 基本的なTypeScript/JavaScriptの知識
- （オプション）Docker（RuVector PostgreSQL利用時）
- （オプション）Git、GitHub CLI（GitHub統合時）
- マルチエージェントシステムの基本概念理解（推奨）
