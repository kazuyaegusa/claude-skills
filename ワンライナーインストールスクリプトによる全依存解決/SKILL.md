# ワンライナーインストールスクリプトによる全依存解決

> Linux/macOS/WSL2でPython・Node.js・全依存関係・`hermes`コマンドまでを1コマンドで自動セットアップする

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

手動で依存関係を揃えるのは時間がかかり、環境差異でエラーが起きやすい。ワンライナーインストーラーなら、gitさえあれば誰でも2分で動作環境を構築できる

## いつ使うのか

新しい環境でHermes Agentを素早くセットアップしたいとき、手動依存管理を避けたいとき

## やり方

1. `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash` を実行
2. インストーラーがPython・Node.js・依存パッケージ・`hermes`コマンドを自動セットアップ
3. `source ~/.bashrc` (または `source ~/.zshrc`) でシェルをリロード
4. `hermes`コマンドで即座に会話開始可能

### 入力

- git
- インターネット接続

### 出力

- 完全セットアップ済みHermes Agent環境
- `hermes`コマンド

## 使うツール・ライブラリ

- curl
- bash
- Hermes Agent install script

## コード例

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes
```

## 前提知識

- Linux/macOS/WSL2環境（Windows nativeは非対応）
- git
- LLMプロバイダーAPIキー（OpenRouter/OpenAI/Anthropic/Kimi/MiniMax等のいずれか）
- Python 3.11+ (インストーラーが自動セットアップ)
- Node.js (インストーラーが自動セットアップ)
- Telegram/Discord等のBot Token（メッセージングゲートウェイ利用時）
- Daytona/Modalアカウント（サーバーレス利用時、オプション）

## 根拠

> 「curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash」
