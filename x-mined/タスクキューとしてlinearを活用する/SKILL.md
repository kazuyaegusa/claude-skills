# タスクキューとしてLinearを活用する

> LinearのIssueをAIエージェントへのジョブ投入口として使い、ステータス（not human / human / human review）でタスクのライフサイクルを管理する。

- 出典: https://x.com/ai_agent_dev/status/2027950582804451451?s=46
- 投稿者: 遠藤巧巳 - AIネイティブな会社の作り方
- カテゴリ: agent-orchestration

## なぜ使うのか

既存のプロジェクト管理UIをそのまま使えるため、エージェント専用のキューUIを別途構築する必要がなく、人間側の操作コストがゼロになる。

## いつ使うのか

Linearをすでに使っており、AIエージェントへのタスク投入に新しいUIを作りたくない場合。

### 具体的な適用場面

- 個人または小チームが定型タスク（コード生成・調査・ドキュメント作成）をLinearで管理しており、AIに委譲したい場合
- 常時稼働のLinuxマシン（自宅PC・VPS・Raspberry Pi等）があり、サーバーレスを使わず自前でエージェントを動かしたい場合
- AIの出力を即座に本番反映せず、必ず人間のレビューを挟みたいワークフローを設計する場合

## やり方

1. LinearのIssueにラベルまたはフィールドで『担当者種別』を設定（例: assignee=bot, assignee=human）。2. ポーリングスクリプトからLinear APIでフィルタリングして未処理タスクを取得。3. 処理完了後にIssueのステータスを『Human Review』に変更し、結果をコメントとして投稿。

### 入力

- Linear APIトークン
- タスク種別を示すラベル・フィールドの設計

### 出力

- 処理済みIssue（Human Reviewステータス）
- 実行結果コメント

## 使うツール・ライブラリ

- Linear API
- linear-sdk（Node.js）または requests（Python）

## コード例

```
# Linear APIでnot humanタスクを取得する例
import requests

headers = {"Authorization": LINEAR_API_KEY}
query = '''
{
  issues(filter: { assignee: { name: { eq: "bot" } }, state: { name: { neq: "Human Review" } } }) {
    nodes { id title description }
  }
}
'''
resp = requests.post("https://api.linear.app/graphql", json={"query": query}, headers=headers)
tasks = resp.json()["data"]["issues"]["nodes"]
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
