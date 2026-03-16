# 役割特化エージェントによる並列オーケストレーション

> Sisyphus（メインエージェント、Opus 4.5 High）を中心に、Oracle（GPT 5.2 Medium：設計・デバッグ）、Frontend Engineer（Gemini 3 Pro：UI/UX）、Librarian（Sonnet 4.5：ドキュメント検索）、Explore（Grok Code：高速コードベース探索）など専門エージェントを並列実行する

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

単一エージェントだとコンテキストが肥大化し、途中で止まったり精度が落ちる。役割を分けることで各エージェントのコンテキストを軽く保ち、並列実行で速度と品質を両立できる

## いつ使うのか

複雑なタスク、複数ドメインにまたがるタスク、大規模コードベースの変更、LLMが途中で止まる問題が頻発する場合

## やり方

1. OhMyOpenCodeプラグインをOpenCodeにインストール
2. `oh-my-opencode.json`で各エージェントのモデル・温度・パーミッションを定義
3. メインエージェント（Sisyphus）がタスクを分析し、必要に応じてOracle/Librarian/Exploreをバックグラウンド起動
4. 各エージェントの結果をSisyphusが統合し、最終的なコード変更を実行
5. `ultrawork`または`ulw`キーワードをプロンプトに含めることで、全機能が自動的に発動

### 入力

- OpenCode環境
- 複数のLLM APIキー（Claude, GPT, Gemini, Grok等）
- タスク記述（プロンプト）

### 出力

- 役割分担された複数エージェントによる並列実行
- コンテキスト効率化による高速・高精度な実装
- 途中停止せず完了まで継続する実行

## 使うツール・ライブラリ

- oh-my-opencode (npm package)
- OpenCode
- LSP (Language Server Protocol)
- AST-Grep
- Exa (web search MCP)
- Context7 (documentation MCP)
- Grep.app (GitHub code search MCP)

## コード例

```
// プロンプト例
// 「ulw この機能を実装してください」だけで、エージェントが自動的に:
// - コードベース構造を分析（Explore）
// - 公式ドキュメント・既存実装を検索（Librarian）
// - 設計判断・デバッグ（Oracle）
// - フロントエンド実装（Frontend Engineer）
// - メイン実装統合（Sisyphus）
// を並列実行し、完了まで継続
```

## 前提知識

- OpenCodeの基本的な使い方
- LLM API（Claude, GPT, Gemini等）のアクセス権
- npm/Node.js環境
- マルチエージェントオーケストレーションの概念理解
- LSP/ASTの基本的な理解（リファクタリング機能を使う場合）
