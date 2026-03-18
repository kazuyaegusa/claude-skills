# Agent BoosterによるLLMスキップ高速編集

> 単純なコード変換（var→const、型注釈追加等）をRust/WASM実装で<1ms処理し、LLM APIを呼ばずに352倍高速化、コスト$0

- 出典: https://github.com/ruvnet/ruflo
- 投稿者: ruvnet
- カテゴリ: agent-orchestration

## なぜ使うのか

LLM呼び出しは1回あたり2-5秒+$0.0002-0.015かかる。機械的な編集にLLMは不要で、WebAssemblyで直接AST操作すれば圧倒的に速く安い

## いつ使うのか

1000ファイルの一括リネーム、全ファイルへのimport追加、型注釈の自動付与など、パターンが明確な大量編集

## やり方

1. Hooksシステムが`pre-task`で複雑度を判定
2. 単純変換（var-to-const、add-types等）なら`[AGENT_BOOSTER_AVAILABLE]`シグナル出力
3. `npx agentic-flow agent-booster edit --file src/api.ts --instructions "Add error handling" --code 'try { ... }'`でWASM実行
4. AST解析→変換→書き戻しが<1msで完了
5. LLM呼び出しをスキップしてコスト削減

### 入力

- 変換インテント（var-to-const, add-types, add-error-handling等）
- 対象ファイルまたはglob
- （オプション）変換ルール

### 出力

- 変換後のコード
- 実行時間（通常<1ms）
- コスト削減額（LLM呼び出しとの差分）

## 使うツール・ライブラリ

- agentic-flow（Agent Booster WASM）
- @claude-flow/hooks（複雑度判定、ルーティング）

## コード例

```
// 1000ファイルの変数名変更
npx agentic-flow agent-booster batch-rename --pattern "getUserData" --replacement "fetchUserProfile" --glob "src/**/*.ts"
// 時間: 1秒（LLMなら5.87分）、コスト: $0（LLMなら$10/日）
```

## 前提知識

- Node.js 20+とnpm 9+
- Claude Code CLIのインストール（`npm install -g @anthropic-ai/claude-code`）
- Anthropic APIキー（Claude利用時）またはClaude Codeサブスクリプション
- 基本的なTypeScript/JavaScriptの知識
- （オプション）Docker（RuVector PostgreSQL利用時）
- （オプション）Git、GitHub CLI（GitHub統合時）
- マルチエージェントシステムの基本概念理解（推奨）

## 根拠

> 「Production-ready multi-agent AI orchestration for Claude Code」「Deploy 60+ specialized agents in coordinated swarms with self-learning capabilities」

> 「Agent Booster (WASM) skips LLM for simple edits (<1ms) ... 352x faster than LLM」

> 「3-tier model routing: Tier 1 (Agent Booster, $0) → Tier 2 (Haiku, $0.0002) → Tier 3 (Opus, $0.015)」「75% lower costs」

> 「AIDefence threat detection (<10ms) ... 50+ patterns ... prompt injection, jailbreak, PII scanning」

> 「Context Autopilot (ADR-051) ... archives, optimizes, and restores conversation context automatically ... never lose context to compaction」
