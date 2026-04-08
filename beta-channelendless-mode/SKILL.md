# Beta Channel（Endless Mode）

> 生体模倣メモリアーキテクチャで超長期セッション（数時間〜数日）を実現する実験機能

- 出典: https://github.com/thedotmack/claude-mem
- 投稿者: thedotmack
- カテゴリ: claude-code-workflow

## なぜ使うのか

通常のセッション終了→要約圧縮では、リアルタイムの文脈が失われる。Endless Modeは進行中セッションの短期記憶と過去セッションの長期記憶を分離し、生物の記憶メカニズムを模倣することで継続性を高める

## いつ使うのか

1つのタスクが数時間〜数日続く大規模リファクタリングや調査タスクで、セッションを切らずに継続したい場合

## やり方

1. Web Viewer UI（http://localhost:37777）→ Settings → Beta Channelに切り替え 2. 再起動後、短期メモリバッファが有効化 3. 定期的なメモリ統合ジョブで短期→長期に転送

### 入力

- 進行中セッションの短期Observation
- 過去セッションの長期要約

### 出力

- 統合された継続的コンテキスト

## 使うツール・ライブラリ

- Beta版Worker
- 短期メモリバッファ（実装詳細は非公開）

## コード例

```
// Beta Channel有効化（概念）
// settings.json
{ "betaChannel": true }
```

## 前提知識

- Claude Codeの基本的な使い方（ツール使用、セッション概念）
- Node.js 18+のインストール
- SQLiteの基本知識（オプション：データ構造理解のため）
- MCP（Model Context Protocol）の概念（オプション：検索ツール理解のため）

## 根拠

> 「Beta Features: Endless Mode (biomimetic memory architecture for extended sessions)」

> 「Worker Service - HTTP API on port 37777 with web viewer UI and 10 search endpoints, managed by Bun」
