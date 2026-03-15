# 自宅常駐PCをエージェント基盤として活用する

> クラウドサーバーを使わず、自宅の常時起動LinuxPCをエージェントの実行基盤として使うアーキテクチャを採用する。

- 出典: https://x.com/ai_agent_dev/status/2027950582804451451?s=46
- 投稿者: 遠藤巧巳 - AIネイティブな会社の作り方
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeのサブスクリプション認証はローカルCLIに紐付いているため、クラウド上のサーバーでは認証が複雑になる。自宅PCなら既存の認証環境をそのまま使え、追加コストゼロでエージェントを常駐させられる。

## いつ使うのか

個人利用でクラウドコストを抑えたい場合、またはClaude CLIのサブスクリプション認証をそのまま使いたい場合。

### 具体的な適用場面

- 個人または小チームが定型タスク（コード生成・調査・ドキュメント作成）をLinearで管理しており、AIに委譲したい場合
- 常時稼働のLinuxマシン（自宅PC・VPS・Raspberry Pi等）があり、サーバーレスを使わず自前でエージェントを動かしたい場合
- AIの出力を即座に本番反映せず、必ず人間のレビューを挟みたいワークフローを設計する場合

## やり方

1. 自宅Linuxマシンのスリープ・シャットダウンを無効化（`sudo systemctl mask sleep.target suspend.target hibernate.target`）。2. cronまたはsystemdタイマーでポーリングスクリプトを登録。3. Claude CLIのセットアップ（`claude`コマンドが使える状態）を確認。4. ネットワーク断時の再試行ロジックをスクリプトに組み込む。

### 入力

- 常時稼働可能なLinuxマシン
- Claude CLIインストール済み・ログイン済み環境

### 出力

- 24時間稼働するパーソナルエージェント基盤

## 使うツール・ライブラリ

- systemd
- cron
- claude CLI

## コード例

```
# systemdタイマーによる定期実行（cron代替）
# /etc/systemd/system/linear-agent.timer
[Timer]
OnBootSec=1min
OnUnitActiveSec=10min

[Install]
WantedBy=timers.target
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
