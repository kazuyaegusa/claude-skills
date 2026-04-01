# LSP/AST統合リファクタリング

> Language Server Protocol（LSP）とAST-Grepを活用し、テキスト検索・置換ではなく、意味論的に正確なコード変更を実行する

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

grepやテキスト検索は文字列マッチのみで、変数スコープや型情報を考慮しない。LSPは言語の意味を理解しているため、誤った置換や見落としがなく、安全かつ決定的なリファクタリングが可能

## いつ使うのか

関数・変数・クラス名の変更、コード構造の再編成、型定義の変更等、安全性が重要なリファクタリング

## やり方

1. リファクタリングタスク（例：関数名変更、変数リネーム）を受け取る
2. grepではなくLSPツール（rename、references、diagnostics等）を使用
3. LSPが言語サーバーと通信し、意味論的に正確な変更箇所を特定
4. 全ての参照箇所を漏れなく変更
5. 型チェック・リント結果を即座に確認

### 入力

- リファクタリング対象（シンボル名、ファイルパス等）
- LSP設定（言語サーバー）

### 出力

- 意味論的に正確な変更
- 全参照箇所の一括更新
- 型エラー・リントエラーの即座検出

## 使うツール・ライブラリ

- oh-my-opencode plugin（LSP integration）
- AST-Grep
- 各言語のLanguage Server（typescript-language-server、rust-analyzer等）

## コード例

```
// LSP rename example（内部動作）
// ユーザー: "Rename function 'oldName' to 'newName'"
lsp.rename({
  file: 'src/utils.ts',
  position: { line: 10, character: 9 },
  newName: 'newName'
});
// -> LSPが全ファイルの参照箇所を自動検出・変更
```

## 前提知識

- OpenCode または Claude Code の基本理解
- LLMエージェント（Claude、GPT、Gemini等）の概念
- LSP（Language Server Protocol）の基本知識
- マルチエージェント・オーケストレーションの概念
