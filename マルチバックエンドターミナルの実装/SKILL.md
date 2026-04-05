# マルチバックエンドターミナルの実装

> エージェントの実行環境を6種類（local, Docker, SSH, Daytona, Singularity, Modal）から選択可能にし、ラップトップ以外で動作させる

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

ラップトップに縛られると、閉じたらエージェントが停止し、リソースも占有される。サーバーレス環境やVPSで動かすことで、アイドル時コストほぼゼロ＋常時稼働が可能

## いつ使うのか

ラップトップを閉じてもエージェントを動かし続けたい、コストを最小化したい、GPUリソースが必要、複数環境で使いたい場合

## やり方

1. ターミナルバックエンドを抽象化（local/Docker/SSH/Daytona/Singularity/Modal）
2. Daytona/Modalではサーバーレス永続化を実装（アイドル時休止、要求時復帰）
3. `hermes` CLIでバックエンドを選択
4. SSHバックエンドで$5 VPSやGPUクラスタに接続
5. Dockerで環境隔離、Singularityでスパコン環境対応

### 入力

- ターミナルバックエンドの選択（CLI引数または設定）
- SSH/API認証情報（必要に応じて）

### 出力

- 指定バックエンドで動作するエージェント環境
- サーバーレスの場合はアイドル時休止＋復帰

## 使うツール・ライブラリ

- Daytona（サーバーレス開発環境）
- Modal（サーバーレスコンピューティング）
- Docker
- SSH
- Singularity（HPC向けコンテナ）

## コード例

```
hermes --backend modal
hermes --backend ssh --ssh-host myserver.com
hermes --backend daytona
```

## 前提知識

- Linux/macOS/WSL2環境（WindowsネイティブはWSL2必須）
- git（インストールスクリプトの唯一の前提条件）
- LLMプロバイダーのAPIキー（Anthropic, OpenRouter, OpenAI等）
- （オプション）メッセージングプラットフォームのBot認証トークン
- （オプション）SSH/Daytona/Modal等のバックエンド認証情報

## 根拠

> "Six terminal backends — local, Docker, SSH, Daytona, Singularity, and Modal. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions."
