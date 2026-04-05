# プライバシー制御（<private>タグ）

> センシティブな情報を `<private>...</private>` で囲むことで、観測ストレージから除外する

- 出典: https://github.com/thedotmack/claude-mem
- 投稿者: thedotmack
- カテゴリ: claude-code-workflow

## なぜ使うのか

APIキー・パスワード・個人情報をメモリに保存したくない。タグベースの除外で、保存対象を細かく制御

## いつ使うのか

機密情報を含むセッションで、特定の内容だけメモリから除外したい時

## やり方

1. センシティブな内容を `<private>APIキー: xxx</private>` で囲む
2. PostToolUseフックがタグを検出し、該当部分を観測データから除外
3. ログにも記録されない

### 入力

- `<private>` タグで囲まれたテキスト

### 出力

- タグ内容を除外した観測データ

## 使うツール・ライブラリ

- PostToolUseフック（タグパーサー）

## コード例

```
// 使用例
<private>
ANTHROPIC_API_KEY=sk-ant-xxx
</private>

// フック内部処理
if (content.includes('<private>')) {
  content = content.replace(/<private>.*?<\/private>/gs, '[REDACTED]');
}
```

## 前提知識

- Claude Codeの基本操作とプラグインシステムの理解
- Node.js 18.0.0+の実行環境
- SQLiteの基本概念（テーブル、クエリ）
- ベクトル検索・埋め込みの基礎知識（Chroma理解のため）
- ライフサイクルフック・イベント駆動設計の概念
- TypeScript/JavaScript（カスタマイズ時）
