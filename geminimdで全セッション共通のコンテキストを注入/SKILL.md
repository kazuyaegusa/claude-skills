# GEMINI.mdで全セッション共通のコンテキストを注入

> プロジェクトルートまたは `~/.gemini/` に `GEMINI.md` を配置し、プロンプトに自動追加される指示を記述する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

コーディング規約、プロジェクト固有の制約、頻出コマンド等を毎回説明する手間を省き、一貫した応答を得られる

## いつ使うのか

複数セッションで同じコンテキストを共有したい場合、チーム全体で統一した指示を共有したい場合

## やり方

1. プロジェクトルートに `GEMINI.md` を作成
2. マークダウン形式で指示を記述（例: 「Python 3.12+を使用」「dataclass必須」）
3. Gemini CLIを起動すると自動で読み込まれる
4. グローバル設定は `~/.gemini/GEMINI.md` に記述

### 入力

- マークダウン形式の指示ファイル（GEMINI.md）

### 出力

- 全プロンプトに自動追加されるコンテキスト
- 一貫した応答品質

## 使うツール・ライブラリ

- Gemini CLI
- Markdown

## コード例

```
# GEMINI.md

## Coding Rules
- Python 3.12+
- Use dataclass for models
- async/await for all I/O
```

## 前提知識

- Node.js 18以上の基本的な理解
- ターミナル操作の基礎知識
- npmパッケージマネージャーの基本的な使い方
- LLM APIの基本概念（プロンプト、トークン、コンテキストウィンドウ）
- OAuth認証フローの概要理解（ブラウザベース認証）
- JSON形式の基本的なパース方法
- （GitHub Actions利用の場合）GitHub Actionsの基本構文
- （MCP利用の場合）Model Context Protocolの概要

## 根拠

> 「Powerful Gemini 3 models: Access to improved reasoning and 1M token context window」（Gemini 3モデル、1Mトークンコンテキスト）

> 「Run instantly with npx: npx @google/gemini-cli」（npxで即時実行可能）

> 「Non-interactive mode for scripts: gemini -p 'Explain the architecture of this codebase' --output-format json」（スクリプト向け非対話モード、JSON出力）

> 「Configure MCP servers in ~/.gemini/settings.json」（settings.jsonでMCP設定）

> 「Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action」（GitHub Actions統合）
