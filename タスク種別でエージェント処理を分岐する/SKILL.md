# タスク種別でエージェント処理を分岐する

> タスクに『not human（AIが自律実行）』と『human（AIがリサーチのみ実行）』の2種別を設け、種別に応じて実行モードを切り替える。

- 出典: https://x.com/ai_agent_dev/status/2027950582804451451?s=46
- 投稿者: 遠藤巧巳 - AIネイティブな会社の作り方
- カテゴリ: agent-orchestration

## なぜ使うのか

全タスクをAIに自律実行させると誤操作リスクが高いが、調査・下書きはAIに任せることで人間のレビュー負荷を下げつつ安全性を確保できる。実行の自律度と安全性のトレードオフを種別で明示的にコントロールする設計。

## いつ使うのか

コード実行・外部API操作などリスクある操作と、情報収集・ドキュメント作成などローリスク操作を同じパイプラインで扱いたいとき。

### 具体的な適用場面

- 個人または小チームが定型タスク（コード生成・調査・ドキュメント作成）をLinearで管理しており、AIに委譲したい場合
- 常時稼働のLinuxマシン（自宅PC・VPS・Raspberry Pi等）があり、サーバーレスを使わず自前でエージェントを動かしたい場合
- AIの出力を即座に本番反映せず、必ず人間のレビューを挟みたいワークフローを設計する場合

## やり方

1. Linearのラベルまたはカスタムフィールドで `execution_type: auto | research` を定義。2. ポーリングスクリプトでフィールド値を読み取り条件分岐。3. `auto`の場合: claude -pでタスク実行 → 結果をIssueに反映。4. `research`の場合: claude -pでリサーチプロンプトを実行 → 調査結果をコメントに投稿し Human Review状態へ。

### 入力

- タスク種別フィールド（LinearカスタムフィールドまたはLabel）

### 出力

- autoタスク: 完了済み成果物
- researchタスク: 調査結果コメント + Human Reviewステータス

## 使うツール・ライブラリ

- Linear API（カスタムフィールド設定）

## コード例

```
for task in tasks:
    if task["executionType"] == "auto":
        result = run_claude(f"以下のタスクを実行してください:\n{task['description']}")
        post_comment(task["id"], result)
    elif task["executionType"] == "research":
        result = run_claude(f"以下についてリサーチしてください:\n{task['description']}")
        post_comment(task["id"], f"## リサーチ結果\n{result}")
    set_status(task["id"], "Human Review")
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
