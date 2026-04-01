# 課題管理とレポート生成をissue.shで自動化する

> scripts/issue.sh を用いて作業課題を登録・更新・完了管理し、完了時に自動的にレポートを生成してリポジトリに記録する

- 出典: https://x.com/0x71ff/status/2035407844502368753
- 投稿者: 0x71
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code が複数の作業を並行実行すると「今何をやっているのか」「何が完了したのか」が不明瞭になる。issue.sh で各作業をトラッキングし、完了時にレポート自動生成すれば、人間は「何が終わったか」を一目で把握できる

## いつ使うのか

Claude Code に複数のタスクを依頼して、進捗と成果物を記録したいとき。「何をやったのか」を後から振り返りたいとき

### 具体的な適用場面

- Proxmox VE / Ceph / GlusterFS / LINSTOR などの分散ストレージを物理サーバで比較評価したいとき
- ベアメタルサーバを繰り返しOS再インストールして検証する必要があるとき
- Supermicro IPMI / Dell iDRAC の操作を自動化したいが、手動スクリプト保守が面倒なとき
- 複数のClaude Codeセッションが同じクラスタを同時操作してもロック機構で安全に制御したいとき

## やり方

1. scripts/issue.sh create "課題タイトル" で新しい課題を登録 (data/issues/ 以下にJSON形式で保存)
2. Claude Code が作業を進める間、scripts/issue.sh update <issue_id> "進捗メモ" で状態を更新
3. 作業完了時、scripts/issue.sh complete <issue_id> でステータスを完了に変更し、自動的に data/reports/ 以下にレポート (Markdown) を生成
4. レポートには作業内容、実行したコマンド、ベンチマーク結果などを含める

### 入力

- 課題タイトル・説明
- 作業中の進捗メモ

### 出力

- 課題一覧 (data/issues/*.json)
- 作業完了レポート (data/reports/YYYY-MM-DD_<issue_name>.md)

## 使うツール・ライブラリ

- jq (JSON操作)
- POSIX sh

## コード例

```
#!/bin/sh
set -eu

COMMAND="${1}"
ISSUE_ID="${2:-}"
MESSAGE="${3:-}"

case "$COMMAND" in
  create)
    ISSUE_ID=$(date +%s)
    echo '{"id": "'$ISSUE_ID'", "title": "'$MESSAGE'", "status": "open"}' > data/issues/$ISSUE_ID.json
    echo "Issue $ISSUE_ID created"
    ;;
  update)
    jq '.status = "in_progress" | .notes += ["'$MESSAGE'"]' data/issues/$ISSUE_ID.json > tmp && mv tmp data/issues/$ISSUE_ID.json
    ;;
  complete)
    jq '.status = "completed"' data/issues/$ISSUE_ID.json > tmp && mv tmp data/issues/$ISSUE_ID.json
    # レポート生成
    TITLE=$(jq -r '.title' data/issues/$ISSUE_ID.json)
    echo "# $TITLE" > data/reports/$(date +%Y-%m-%d)_$ISSUE_ID.md
    echo "Completed at $(date)" >> data/reports/$(date +%Y-%m-%d)_$ISSUE_ID.md
    ;;
esac
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
