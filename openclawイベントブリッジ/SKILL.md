# OpenClawイベントブリッジ

> Claude Codeのセッション開始・終了・ツール実行前後などのイベントを、設定したOpenClawゲートウェイにHTTP POSTで転送し、外部自動化ワークフローをトリガー

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeセッション単体だと外部システム（CI/CD、通知、ログ集約）と連携できない。イベント駆動アーキテクチャで、Claude実行をトリガーとした自動テスト・デプロイ・レポート生成などを実現

## いつ使うのか

Claude Codeをチーム開発フロー・CI/CDパイプライン・DevOpsワークフローに組み込みたい場合。個人の単発作業では不要

## やり方

1. `/oh-my-claudecode:configure-notifications` で対話的セットアップ、または手動で `~/.claude/omc_config.openclaw.json` 作成
2. JSON内で `gateways` にURL・認証ヘッダー・タイムアウトを定義
3. `hooks` で各イベント（session-start, stop, keyword-detector, ask-user-question, pre-tool-use, post-tool-use）ごとにgateway指定 + instruction（テンプレート変数 {{sessionId}}, {{projectName}} 使用可）
4. 環境変数 `OMC_OPENCLAW=1` で有効化（`OMC_OPENCLAW_DEBUG=1` でデバッグログ）
5. OpenClawゲートウェイ側で受信したイベントに応じてアクション実行（例: Discord通知、DB記録、後続タスク起動）

### 入力

- OpenClawゲートウェイURL・認証情報
- イベントフック設定（session-start, stop等）
- 環境変数 OMC_OPENCLAW=1

### 出力

- 各イベント発生時のHTTP POSTリクエスト（JSON payload）
- OpenClawゲートウェイ側での後続処理（通知・ログ・自動化）

## 使うツール・ライブラリ

- OpenClaw（ゲートウェイ）
- OMC
- （オプション）Discord/Slack webhook（ゲートウェイから通知する場合）

## コード例

```
// ~/.claude/omc_config.openclaw.json
{
  "enabled": true,
  "gateways": {
    "my-gateway": {
      "url": "https://your-gateway.example.com/wake",
      "headers": {"Authorization": "Bearer YOUR_TOKEN"},
      "method": "POST",
      "timeout": 10000
    }
  },
  "hooks": {
    "session-start": {
      "gateway": "my-gateway",
      "instruction": "Session started for {{projectName}}",
      "enabled": true
    },
    "stop": {
      "gateway": "my-gateway",
      "instruction": "Session stopping for {{projectName}}",
      "enabled": true
    }
  }
}

# 環境変数で有効化
export OMC_OPENCLAW=1
export OMC_OPENCLAW_DEBUG=1  # デバッグ用
```

## 前提知識

- Claude Code CLIの基本操作（インストール・認証済み）
- tmuxの基礎知識（ペイン・セッション概念）
- Claude Max/Proサブスクリプション または Anthropic APIキー
- （オプション）Codex CLI・Gemini CLIのインストール（マルチAI機能使用時）
- （オプション）OpenClawゲートウェイ構築知識（外部連携時）
- Node.js/npm環境（OMC npmパッケージインストール用）

## 根拠

> "Multi-agent orchestration for Claude Code. Zero learning curve."

> "Enable Claude Code native teams in ~/.claude/settings.json: {\"env\": {\"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS\": \"1\"}}"

> "omc ask claude \"review this migration plan\" → saves markdown artifact under .omc/artifacts/ask/"

> "hooks: session-start, stop, keyword-detector, ask-user-question, pre-tool-use, post-tool-use (6 active in bridge.ts)"
