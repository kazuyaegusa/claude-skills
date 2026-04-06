# SSHリレーサーバーによるリモート通知転送

> SSH/devcontainer/Codespaces環境で音声・通知リクエストをHTTP経由でローカルマシンのリレーサーバーに転送し、ローカルスピーカー・通知で再生する

- 出典: https://github.com/PeonPing/peon-ping
- 投稿者: PeonPing
- カテゴリ: agent-orchestration

## なぜ使うのか

リモートサーバーやコンテナには音声出力デバイスがなく、通知も届かない。ローカルマシンで軽量HTTPサーバーを起動し、リモート側からリクエストを受け取ることで、開発者の手元で通知を受け取れる

## いつ使うのか

SSH経由でリモートサーバー開発、devcontainer、GitHub Codespaces等でAIエージェントを使う時、ローカルマシンで音声・通知を受け取りたい場合

## やり方

1. ローカルマシンで`peon relay --daemon`を実行（ポート19998でリッスン、バックグラウンド起動）
2. SSHログイン時に`ssh -R 19998:localhost:19998 user@server`でポートフォワーディング設定
3. リモート側のpeon.shがSSH環境変数（SSH_CLIENT/SSH_TTY）またはREMOTE_CONTAINERS/CODESPACES変数を検出
4. 音声再生時、ローカルファイルパスではなく`http://127.0.0.1:19998/play?category=<category>`にGETリクエスト
5. リレーサーバーがローカルのconfig.jsonとパックマニフェストを読み込み、カテゴリに応じた音声を選択・再生
6. 通知も同様に`POST /notify`でリレーに送信、ローカルで表示

### 入力

- ローカルマシンのpeon-pingインストール（リレーサーバー機能含む）
- SSHポートフォワーディング（-R 19998:localhost:19998）またはdocker host.docker.internal
- リモート側のpeon-pingまたは軽量フックスクリプト

### 出力

- リモート環境のイベントがローカルスピーカーで音声再生
- ローカルデスクトップに通知表示

## 使うツール・ライブラリ

- Python http.server（リレーサーバー実装）
- curl（リモート→リレーのHTTPリクエスト）
- SSH -R（リバースポートフォワーディング）

## コード例

```
# ローカル
peon relay --daemon

# SSH接続
ssh -R 19998:localhost:19998 user@server

# リモート側フック（scripts/remote-hook.sh）
RELAY_URL="http://127.0.0.1:19998"
EVENT=$(cat | python3 -c "import sys,json; print(json.load(sys.stdin).get('hook_event_name',''))")
case "$EVENT" in
  SessionStart) CATEGORY="session.start" ;;
  Stop) CATEGORY="task.complete" ;;
  PermissionRequest) CATEGORY="input.required" ;;
esac
curl -sf "${RELAY_URL}/play?category=${CATEGORY}" >/dev/null 2>&1 &
```

## 前提知識

- Claude Code/Cursor/Windsurf等のフック機能を持つAI開発環境の基礎知識
- シェルスクリプト（bash/PowerShell）の基本的な読み書き
- JSON設定ファイルの編集経験
- SSH/devcontainer/Codespacesの基本（リモート通知機能を使う場合）
- Model Context Protocol（MCP）の概念（MCP機能を使う場合）

## 根拠

> 「Coding on a remote server or inside a container? peon-ping auto-detects SSH sessions, devcontainers, and Codespaces, then routes audio and notifications through a lightweight relay」（リモート対応の自動検出機能）
