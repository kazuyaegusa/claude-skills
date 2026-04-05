# Progressive Disclosure（段階的開示）

> 文脈を「インデックス（軽量）→タイムライン（中程度）→詳細（重量）」の3層で取得し、必要最小限のトークンで関連情報を引き出す

- 出典: https://github.com/thedotmack/claude-mem
- 投稿者: thedotmack
- カテゴリ: claude-code-workflow

## なぜ使うのか

全過去履歴を毎回注入するとトークンコストが爆発する。検索→フィルタ→詳細取得の段階化で、トークン使用量を従来の1/10に削減

## いつ使うのか

過去の膨大なセッション履歴から特定の情報だけを効率的に引き出したい時

## やり方

1. `search` MCPツールでインデックス取得（1結果50-100トークン）
2. `timeline` で時系列文脈を確認（中程度トークン）
3. 関連IDのみ `get_observations` で詳細取得（1結果500-1,000トークン）
4. Claude Codeはこの3ステップをクエリに応じて自動実行

### 入力

- 検索クエリ（自然言語）
- フィルタ条件（type, date, project）

### 出力

- 段階的に絞り込まれた観測データ
- トークンコスト表示

## 使うツール・ライブラリ

- MCP (Model Context Protocol)
- SQLite FTS5（全文検索）
- Chroma vectorDB（セマンティック検索）

## コード例

```
// Step 1: 軽量インデックス取得
const index = await mcp.search({ query: 'auth bug', limit: 10 });
// Step 2: 興味あるID特定（例: #123, #456）
// Step 3: 詳細取得
const details = await mcp.get_observations({ ids: [123, 456] });
```

## 前提知識

- Claude Codeの基本操作とプラグインシステムの理解
- Node.js 18.0.0+の実行環境
- SQLiteの基本概念（テーブル、クエリ）
- ベクトル検索・埋め込みの基礎知識（Chroma理解のため）
- ライフサイクルフック・イベント駆動設計の概念
- TypeScript/JavaScript（カスタマイズ時）

## 根拠

> 「Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.」

> 「Progressive Disclosure - Layered memory retrieval with token cost visibility」

> 「Install with a single command: npx claude-mem install」

> 「mem-search Skill - Natural language queries with progressive disclosure」
