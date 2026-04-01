# flock ベースの排他ロック機構で複数Claude Codeセッションを安全に制御する

> scripts/pve-lock.sh を用いて flock(1) ベースの排他ロックを取得し、複数の Claude Code セッションが同じ Proxmox VE クラスタを同時操作しても競合しないようにする

- 出典: https://x.com/0x71ff/status/2035407844502368753
- 投稿者: 0x71
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code は複数のウィンドウで並行実行できるため、同じクラスタに対して「セッションAがCephセットアップ中にセッションBが同じノードを再起動」のような競合が起きうる。flock で排他制御すれば、一度に1つのセッションだけが操作を実行し、他のセッションは待機する

## いつ使うのか

複数のClaude Codeセッションが同じリソース (クラスタ, サーバ, ストレージプール等) を操作する可能性があるとき。競合によるデータ破損や設定不整合を防ぎたいとき

### 具体的な適用場面

- Proxmox VE / Ceph / GlusterFS / LINSTOR などの分散ストレージを物理サーバで比較評価したいとき
- ベアメタルサーバを繰り返しOS再インストールして検証する必要があるとき
- Supermicro IPMI / Dell iDRAC の操作を自動化したいが、手動スクリプト保守が面倒なとき
- 複数のClaude Codeセッションが同じクラスタを同時操作してもロック機構で安全に制御したいとき

## やり方

1. scripts/pve-lock.sh を作成し、内部で exec 200>/var/lock/pve-cluster.lock && flock -x 200 を実行
2. ロック取得後に渡されたコマンドを実行、終了時に自動的にロック解放
3. Claude Code が Proxmox VE 操作を行う際は、必ず scripts/pve-lock.sh -- <実際のコマンド> でラップする
4. 例: scripts/pve-lock.sh -- pvesh create /cluster/ceph/init --network 10.0.0.0/24

### 入力

- ロックファイルパス (/var/lock/pve-cluster.lock 等)
- ロック保護下で実行するコマンド

### 出力

- 排他ロック取得→コマンド実行→ロック解放
- 他のセッションは待機して順次実行

## 使うツール・ライブラリ

- flock(1) (util-linux パッケージ)

## コード例

```
#!/bin/sh
set -eu

LOCKFILE="/var/lock/pve-cluster.lock"

exec 200>"$LOCKFILE"
flock -x 200

# ロック取得後、引数で渡されたコマンドを実行
"$@"

# スクリプト終了時に自動的にロック解放
```

## 前提知識

- Proxmox VE / Ceph / LINSTOR などの分散ストレージ技術の基礎知識
- Supermicro IPMI / Dell iDRAC などのBMC操作経験
- Debian preseed によるOS自動インストールの理解
- Claude Code のスキル定義 (.claude/skills/) の書き方
- POSIX sh / Python によるスクリプト作成スキル

## 根拠

> 投稿本文: 「AIの部分これ。claude codeにBMCの権限全部渡して『好きにやってくれ!』ってしてるだけ。大したことしてないのでみんなやるとよい。」

> README.md: 「Claude Code (AI エージェント) がローカルマシンから SSH 経由で物理サーバを操作し、OS インストールからストレージベンチマークまでを自動化する。」

> README.md: 「排他ロック — pve-lock.sh による flock ベースのロックで、複数の Claude Code セッションが同じクラスタを安全に操作」

> README.md: 「課題管理・レポート追跡 — issue.sh による課題管理と、作業完了時のレポート自動生成」

> scripts/bmc-power.sh: 「#!/bin/sh\nset -eu\n\nBMC_HOST=\"${BMC_HOST}\"\nBMC_USER=\"${BMC_USER}\"\nBMC_PASSWORD=\"${BMC_PASSWORD}\"」
