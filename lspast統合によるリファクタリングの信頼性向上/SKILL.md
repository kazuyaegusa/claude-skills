# LSP/AST統合によるリファクタリングの信頼性向上

> Language Server Protocol（LSP）とAST-Grepを使い、決定論的で安全なコード変更を実現

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

LLMの生成したコードは不確実性があるが、LSPによるシンボル解決・参照検索、ASTによる構造的検索を使うことで、リファクタリング・リネーム・診断が確実になる

## いつ使うのか

リファクタリング、変数・関数・クラスのリネーム、型エラー修正、大規模コード変更

## やり方

1. OhMyOpenCodeがLSPサーバーと統合
2. エージェントがコード変更時、LSPのRename/References/Diagnosticsツールを自動活用
3. AST-Grepで構造的な検索・置換を実行
4. LLMが「なんとなく」置換するのではなく、LSP/ASTが保証する正確な操作を実行

### 入力

- LSP対応言語（TypeScript, Python, Go等）
- LSPサーバー設定

### 出力

- 決定論的なコード変更
- 参照漏れのないリネーム
- 型安全性の保証

## 使うツール・ライブラリ

- LSP (Language Server Protocol)
- AST-Grep
- OpenCode LSP integration

## 前提知識

- OpenCodeの基本的な使い方
- LLM API（Claude, GPT, Gemini等）のアクセス権
- npm/Node.js環境
- マルチエージェントオーケストレーションの概念理解
- LSP/ASTの基本的な理解（リファクタリング機能を使う場合）
