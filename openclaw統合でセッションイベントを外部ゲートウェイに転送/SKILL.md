# OpenClaw統合でセッションイベントを外部ゲートウェイに転送

> Claude Codeセッションの開始・停止・ツール実行などのイベントを、OpenClawゲートウェイ（Discord/Slackボット等）にHTTP POSTして外部ワークフローをトリガーする

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude単体では完結しない業務（セッション完了→Discord通知→チームレビュー→承認→デプロイ）を自動化したい場合、イベント駆動で外部システムと連携する必要がある。OpenClaw統合により、Claude側は何も意識せず自動で外部へイベント送信できる

## いつ使うのか

チーム開発でセッション完了を通知したい、外部CIをトリガーしたい、Discord/SlackボットにClaude作業状況を自動報告させたい場合

## やり方

1. `~/.claude/omc_config.openclaw.json` に gateway URL・headers・hooks設定を記述
2. hooks に `session-start`, `stop`, `pre-tool-use`, `post-tool-use` など6種イベントを定義
3. 各hookに `gateway` (送信先) と `instruction` (テンプレート化されたメッセージ) を設定
4. `OMC_OPENCLAW=1` 環境変数で有効化
5. セッション実行時、該当イベント発火で自動的にPOST送信
6. OpenClawゲートウェイ側で受信→Discord/Slackへ転送

### 入力

- OpenClawゲートウェイのURL・認証トークン
- 送信したいイベント種別（session-start, stop, pre-tool-use等）
- 通知先チャネルID（OPENCLAW_REPLY_CHANNEL/TARGET/THREAD環境変数）

### 出力

- 指定イベント発火時にゲートウェイへHTTP POSTリクエスト送信
- ゲートウェイ経由でDiscord/Slackへ通知転送

## 使うツール・ライブラリ

- OpenClaw Gateway
- oh-my-claudecode OpenClaw bridge (scripts/openclaw-gateway-demo.mjs)

## コード例

```
# ~/.claude/omc_config.openclaw.json
{
  "enabled": true,
  "gateways": {
    "my-gateway": {
      "url": "https://your-gateway.example.com/wake",
      "headers": { "Authorization": "Bearer YOUR_TOKEN" },
      "method": "POST",
      "timeout": 10000
    }
  },
  "hooks": {
    "session-start": { "gateway": "my-gateway", "instruction": "Session started for {{projectName}}", "enabled": true },
    "stop": { "gateway": "my-gateway", "instruction": "Session stopping for {{projectName}}", "enabled": true }
  }
}

# 環境変数
export OMC_OPENCLAW=1
export OMC_OPENCLAW_DEBUG=1
export OPENCLAW_REPLY_CHANNEL=discord
export OPENCLAW_REPLY_TARGET=<channel-id>
```

## 前提知識

- Claude Code CLI インストール済み
- Claude Max/Pro サブスクリプション または Anthropic API キー
- tmux インストール（macOS: brew install tmux / Ubuntu: apt install tmux / Windows: psmux）
- 基本的なコマンドライン操作知識
- YAML/JSON設定ファイルの読み書き
- （オプション）codex CLI / gemini CLI（異種LLM統合を使う場合）

## 根拠

> 「Multi-agent orchestration for Claude Code. Zero learning curve.」

> 「OpenClaw integration: Forward Claude Code session events to an OpenClaw gateway to enable automated responses and workflows」
