# LSPによる決定論的リファクタリング

> コード変更をLSP(Language Server Protocol)経由で実行し、リネームやリファクタリングを安全かつ決定論的に行う

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

LLMによるテキスト置換は不完全で危険。LSPは言語解析に基づき全参照を正確に追跡するため、エージェントのリファクタリング品質が劇的に向上

## いつ使うのか

変数/関数/クラスのリネーム、コード抽出、インライン化など構造変更が必要な場合

## やり方

1. エージェントがリファクタリングの必要性を判断
2. LSPツール(rename, refactor等)を呼び出し
3. LSPがコードベース全体を解析して変更箇所を特定
4. 全ての参照を一括変更
5. 型チェック・リントでバリデーション

### 入力

- 変更対象のシンボル
- 新しい名前または変更内容

### 出力

- 変更されたファイル一覧
- 差分

## 使うツール・ライブラリ

- LSP
- oh-my-opencode LSP integration
- AST-Grep

## コード例

```
// LSP有効化設定
"lsp": {
  "enabled": true,
  "languages": ["typescript", "python", "go"]
}
```

## 前提知識

- OpenCodeまたはClaude Code等のLLMエージェント環境の基本理解
- 複数LLMサブスクリプション(推奨: Claude Pro, ChatGPT Plus, Gemini Advanced)
- コマンドライン操作の基礎知識
- JSONまたはJSONC設定ファイルの編集スキル
- エージェント型開発の概念(プロンプトエンジニアリング、コンテキスト管理等)
