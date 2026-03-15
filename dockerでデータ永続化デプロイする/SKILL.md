# Dockerでデータ永続化デプロイする

> Dockerボリュームを作成してn8nコンテナを起動し、ワークフロー設定を永続化する

- 出典: https://github.com/n8n-io/n8n
- 投稿者: n8n-io
- カテゴリ: automation-pipeline

## なぜ使うのか

コンテナ再起動後もワークフロー・認証情報が消えないよう、`/home/node/.n8n`をボリュームにマウントする

## いつ使うのか

本番またはステージング環境にセルフホストする時、データを永続化したい時

## やり方

1. `docker volume create n8n_data`でボリューム作成
2. `docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n`でコンテナ起動
3. http://localhost:5678 でアクセス

### 入力

- Docker環境

### 出力

- 永続化されたn8nインスタンス（ポート5678）

## 使うツール・ライブラリ

- Docker

## コード例

```
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

## 前提知識

- Node.js（npx起動の場合）またはDocker（コンテナ起動の場合）の基本操作
- ワークフロー自動化の基本概念（トリガー、アクション、条件分岐）
- AIエージェント機能を使う場合はLangChainの基礎知識

## 根拠

> "n8n is a workflow automation platform that gives technical teams the flexibility of code with the speed of no-code."

> npx n8n

> docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
