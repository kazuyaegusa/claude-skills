# cronで10分ポーリングループを構築する

> cronジョブまたはsystemdタイマーでポーリングスクリプトを定期実行し、常駐プロセスなしにエージェントループを維持する。

- 出典: https://x.com/ai_agent_dev/status/2027950582804451451?s=46
- 投稿者: 遠藤巧巳 - AIネイティブな会社の作り方
- カテゴリ: agent-orchestration

## なぜ使うのか

常駐デーモンを自前実装するより、cronを使うほうが障害時の自動再起動・ログ管理・デバッグが容易で、個人インフラには適切な複雑度。

## いつ使うのか

処理時間が10分以内に収まるタスクが中心で、リアルタイム性より安定性を優先する場合。

### 具体的な適用場面

- 個人または小チームが定型タスク（コード生成・調査・ドキュメント作成）をLinearで管理しており、AIに委譲したい場合
- 常時稼働のLinuxマシン（自宅PC・VPS・Raspberry Pi等）があり、サーバーレスを使わず自前でエージェントを動かしたい場合
- AIの出力を即座に本番反映せず、必ず人間のレビューを挟みたいワークフローを設計する場合

## やり方

1. `crontab -e` を開く。2. `*/10 * * * * /path/to/venv/bin/python /path/to/poll_linear.py >> /var/log/linear_agent.log 2>&1` を追加。3. スクリプト内でロックファイル（`/tmp/linear_agent.lock`）を使い多重起動を防ぐ。

### 入力

- 実行可能なポーリングスクリプト
- Pythonまたはシェル環境

### 出力

- 定期実行ログ
- 処理済みタスク

## 使うツール・ライブラリ

- cron
- systemd timer（代替）
- flock（多重起動防止）

## コード例

```
# ロックファイルによる多重起動防止
import fcntl, sys

lock_file = open("/tmp/linear_agent.lock", "w")
try:
    fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOError:
    sys.exit(0)  # 前の実行がまだ動いている
```

## 前提知識

- Linear APIの基本操作（Issue取得・ステータス更新・コメント投稿）
- Claude CLI（`claude`コマンド）のインストールとサブスクリプション認証設定
- Pythonまたはシェルスクリプトによるサブプロセス実行の知識
- cronまたはsystemdタイマーの設定方法
- 常時起動可能なLinux環境の用意

## 根拠

> 「自宅のLinuxPCを起動しておけば、10分に1回Linearのタスクを見にいくようにした」

> 「not humanのタスクを自動的に取得して、Claude -pで実行し、結果をLinearに戻し、human review状態とする」

> 「humanタスクの場合は、リサーチをしてリサーチ結果をLinearに戻して、human review状態とする」

> 「Linearにやりたいことを追加すれば、裏側でClaudeCodeが動く流れができた」
