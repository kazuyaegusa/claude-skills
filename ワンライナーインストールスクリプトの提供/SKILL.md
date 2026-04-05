# ワンライナーインストールスクリプトの提供

> curl | bash 形式のインストールスクリプトで、前提条件なしでエージェントをセットアップする

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

依存関係の手動インストール（Python, Node.js等）はエラーが起きやすく、ユーザー体験を損なう。ワンライナーで全自動化することで、導入障壁を最小化する

## いつ使うのか

新規ユーザーが最速でセットアップしたい、CI/CDで自動インストールしたい場合

## やり方

1. インストールスクリプト（install.sh）をGitHubでホスト
2. スクリプト内でOS検出（Linux/macOS/WSL2）
3. Python, Node.js, 依存パッケージを自動インストール
4. `hermes` コマンドをPATHに追加
5. `.bashrc` / `.zshrc` をリロードするようユーザーに指示

### 入力

- Linux/macOS/WSL2環境
- git（唯一の前提条件）

### 出力

- 完全にセットアップされたHermes Agent環境
- `hermes` コマンド

## 使うツール・ライブラリ

- bash
- curl

## コード例

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

## 前提知識

- Linux/macOS/WSL2環境（WindowsネイティブはWSL2必須）
- git（インストールスクリプトの唯一の前提条件）
- LLMプロバイダーのAPIキー（Anthropic, OpenRouter, OpenAI等）
- （オプション）メッセージングプラットフォームのBot認証トークン
- （オプション）SSH/Daytona/Modal等のバックエンド認証情報

## 根拠

> "curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash"
