# Web Viewer UI（リアルタイム観測フィード）

> http://localhost:37777 でメモリストリームをWebブラウザで可視化・検索・設定管理

- 出典: https://github.com/thedotmack/claude-mem
- 投稿者: thedotmack
- カテゴリ: claude-code-workflow

## なぜ使うのか

CLI外からメモリ状態を確認・デバッグしたい。Web UIでリアルタイム観測フィード + 引用ID確認 + バージョン切り替えが可能

## いつ使うのか

メモリの蓄積状況を可視化したい時、設定を変更したい時

## やり方

1. Workerサービス起動後、ブラウザで http://localhost:37777 にアクセス
2. リアルタイム観測ストリーム表示
3. 検索クエリ入力でFTS5/Chroma検索
4. 設定画面でAIモデル・ポート・ログレベル変更
5. Beta機能（Endless Mode等）のバージョン切り替え

### 入力

- Workerサービス起動済み

### 出力

- Web UI（観測フィード、検索結果、設定画面）

## 使うツール・ライブラリ

- Bun（HTTPサーバー）
- TypeScript（フロントエンド）

## コード例

```
// 観測データAPI
GET http://localhost:37777/api/observation/{id}
GET http://localhost:37777/api/search?q=auth

// Webビューアー
http://localhost:37777
```

## 前提知識

- Claude Codeの基本操作とプラグインシステムの理解
- Node.js 18.0.0+の実行環境
- SQLiteの基本概念（テーブル、クエリ）
- ベクトル検索・埋め込みの基礎知識（Chroma理解のため）
- ライフサイクルフック・イベント駆動設計の概念
- TypeScript/JavaScript（カスタマイズ時）

## 根拠

> 「Web Viewer UI - Real-time memory stream at http://localhost:37777」
