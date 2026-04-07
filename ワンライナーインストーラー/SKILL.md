# ワンライナーインストーラー

> curlで実行する単一スクリプトで、Python/Node.js/依存関係を全自動セットアップ

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

複雑な依存関係や環境構築の手間を排除し、初心者でも即座に使い始められるようにするため。

## いつ使うのか

新規環境で即座にセットアップしたい場合、前提知識なしでインストールしたい場合

## やり方

1. `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`実行 2. スクリプトがPython/Node.js/依存関係を自動インストール 3. `hermes`コマンドが使えるようになる 4. `source ~/.bashrc`でシェル再読み込み

### 入力

- git（必須）

### 出力

- 動作可能な`hermes`コマンド

## 使うツール・ライブラリ

- install.sh

## コード例

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

## 前提知識

- 基本的なコマンドライン操作
- LLM APIキー（OpenRouter/OpenAI/Anthropic等のいずれか）
- gitがインストールされた環境
- Linux/macOS/WSL2のいずれか

## 根拠

> curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
