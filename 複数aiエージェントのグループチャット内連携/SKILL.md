# 複数AIエージェントのグループチャット内連携

> 1つのグループチャットに複数のAIボット（Claude, Gemini等）を参加させ、相互に対話・情報共有させる。

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: agent-orchestration

## なぜ使うのか

異なるLLMはそれぞれ得意分野が異なる。Claudeはコード生成、GeminiはWeb検索・データ分析に強い場合、両者を同じチャットで呼び出せれば、ユーザーは文脈を切り替えずに最適なエージェントに問い合わせできる。

## いつ使うのか

複数のLLMを使い分けたい時。1つのエージェントでは解決できない複雑なタスクを複数エージェントで分担させたい時。

## やり方

1. config.tomlで複数のproject設定を記述（例: project A = Claude + Telegram, project B = Gemini + Telegram）
2. 各projectのボットを同じTelegramグループに招待
3. グループチャットで @ClaudeBot, @GeminiBot のようにメンションして呼び分け
4. cc-connectがmulti-bot relayをサポートしているため、ボット間で情報共有・連鎖応答が可能

### 入力

- 複数のAIエージェント設定（config.toml内の複数project）
- グループチャットの作成とボット招待

### 出力

- グループチャット内で複数AIが協調動作
- 文脈を保ったままエージェント切替

## 使うツール・ライブラリ

- cc-connect（multi-project architecture）

## コード例

```
# config.toml 例
[[projects]]
name = "claude-telegram"
agent = "claude"
platform = "telegram"

[[projects]]
name = "gemini-telegram"
agent = "gemini"
platform = "telegram"

# グループチャットで
@ClaudeBot この関数をリファクタして
@GeminiBot GitHub trending を検索して
```

## 前提知識

- ローカルマシンにNode.js or Go環境（cc-connectインストールに必要）
- Claude Code, Cursor, Gemini CLI等のAIエージェントがインストール済みであること
- メッセンジャープラットフォーム（Telegram/Slack/Discord等）のBot Token取得方法の基礎知識
- TOML形式の設定ファイル編集スキル
- WebSocket/Long Polling等の接続方式の概念理解（必須ではないが理解があると設定が楽）

## 根拠

> 「7 AI Agents — Claude Code, Codex, Cursor Agent, Qoder CLI, Gemini CLI, OpenCode, iFlow CLI.」（7種類のエージェント対応）

> 「9 Chat Platforms — Feishu, DingTalk, Slack, Telegram, Discord, WeChat Work, LINE, QQ, QQ Bot (Official). Most need zero public IP.」（9プラットフォーム対応、公開IP不要）
