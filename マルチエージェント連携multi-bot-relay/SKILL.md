# マルチエージェント連携（Multi-Bot Relay）

> 1つのグループチャットに複数のAIエージェント（Claude, Gemini等）を参加させ、相互に会話・情報交換させる

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: agent-orchestration

## なぜ使うのか

異なる専門性や視点を持つAIエージェントを組み合わせることで、より多角的な分析・意思決定支援が可能になるため

## いつ使うのか

複数の視点から問題を分析したい場合（例: Claudeでコードレビュー→Geminiで代替案提示）、異なる専門性を持つエージェントを組み合わせたい場合

## やり方

1. config.tomlで複数のprojectsセクションを定義し、それぞれ異なるagentを指定（例: project1はclaude-code、project2はgemini）
2. 各プロジェクトを同じチャットグループに参加させる
3. グループチャット内でメンションやコマンドで特定エージェントを呼び出す
4. エージェント同士がメッセージを読み合い、協調して応答する

### 入力

- 複数のAIエージェント設定（config.toml内の[[projects]]を複数定義）
- 同一グループチャットへの参加設定

### 出力

- 複数エージェントが協調して応答するチャット環境

## 使うツール・ライブラリ

- cc-connect
- 複数のAIエージェントCLI

## コード例

```
# config.toml例
[[projects]]
name = "claude-bot"
agent = "claude-code"
platform = "telegram"

[[projects]]
name = "gemini-bot"
agent = "gemini"
platform = "telegram"

# 両方を同じTelegramグループに招待
```

## 前提知識

- ローカル環境にAIエージェント（Claude Code CLI、Cursor、Gemini CLI等）がインストール済みであること
- チャットプラットフォーム（Telegram、Discord、Slack等）のアカウントとBot作成権限
- Node.js（npm経由インストールの場合）またはGo 1.22+（ソースビルドの場合）
- 基本的なコマンドライン操作とTOML設定ファイル編集の知識
- WebSocket/Long Polling等の接続方式の基本理解（トラブルシューティング時）
