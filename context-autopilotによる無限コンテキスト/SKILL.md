# Context Autopilotによる無限コンテキスト

> Claude Codeの20万トークン上限を回避し、ターン単位でSQLiteにアーカイブ+復元することで、事実上無限のコンテキストを実現

- 出典: https://github.com/ruvnet/ruflo
- 投稿者: ruvnet
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeは上限に達すると自動圧縮（compaction）で詳細を失う。Autopilotは圧縮前にアーカイブし、重要度ランク付けで必要な情報を復元することで、長期セッションでも情報損失なし

## いつ使うのか

長期開発セッション（数時間〜数日）で、初期の設計決定や詳細なログを保持したい場合

## やり方

1. UserPromptSubmitフックで毎ターンSQLiteにアーカイブ（SHA-256で重複排除）
2. 実APIの`usage`データでトークン%をリアルタイム追跡
3. 70%でwarning、85%でpruning（古いエントリ削除）、90%でPreCompactフック発火
4. PreCompactは自動圧縮をexit code 2でブロック、手動`/compact`のみ許可
5. SessionStartフックで重要度ランク（recency × frequency × richness）順に復元
6. 30日間未アクセスエントリは自動削除（auto-pruning）

### 入力

- 会話履歴（自動取得）
- 重要度スコアリング設定

### 出力

- SQLiteアーカイブ（.claude-flow/data/transcript-archive.db）
- 復元された上位Kエントリ
- ステータスライン表示（🛡️ 45% 89.2K ⊘）

## 使うツール・ライブラリ

- .claude/helpers/context-persistence-hook.mjs
- SQLite（WALモード）
- RuVector PostgreSQL（オプション、スケーラブル）

## コード例

```
# ステータス確認
node .claude/helpers/context-persistence-hook.mjs status
# アーカイブクエリ
sqlite3 .claude-flow/data/transcript-archive.db "SELECT COUNT(*), SUM(LENGTH(content)) FROM transcript_entries;"
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

> 「Context Autopilot (ADR-051) ... archives, optimizes, and restores conversation context automatically ... never lose context to compaction」
