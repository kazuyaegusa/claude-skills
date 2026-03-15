# claude -pでタスクをノンインタラクティブ実行する

> `claude -p`（print mode）を使い、タスク内容を標準入力またはプロンプト引数として渡してClaudeCodeをスクリプトから非対話実行する。

- 出典: https://x.com/ai_agent_dev/status/2027950582804451451?s=46
- 投稿者: 遠藤巧巳 - AIネイティブな会社の作り方
- カテゴリ: claude-code-workflow

## なぜ使うのか

通常のClaude CLIは対話モードのため自動化に使えないが、`-p`フラグで単発実行・標準出力への結果取得が可能になり、シェルスクリプトやPythonからサブプロセスとして呼び出せる。

## いつ使うのか

PythonやシェルスクリプトからClaudeCodeを自動呼び出ししたいとき。

### 具体的な適用場面

- 個人または小チームが定型タスク（コード生成・調査・ドキュメント作成）をLinearで管理しており、AIに委譲したい場合
- 常時稼働のLinuxマシン（自宅PC・VPS・Raspberry Pi等）があり、サーバーレスを使わず自前でエージェントを動かしたい場合
- AIの出力を即座に本番反映せず、必ず人間のレビューを挟みたいワークフローを設計する場合

## やり方

1. タスクのtitle+descriptionをプロンプト文字列に組み立てる。2. `subprocess.run(["claude", "-p", prompt], capture_output=True, text=True)` で実行。3. `result.stdout` を結果として取得し、Linearのコメントに投稿。4. 環境変数から `ANTHROPIC_API_KEY` を除外してサブスクリプション認証を使う（グローバルCLAUDE.md参照）。

### 入力

- タスクのプロンプト文字列
- Claude CLIがインストール済みの環境

### 出力

- Claudeの実行結果テキスト（stdout）

## 使うツール・ライブラリ

- claude CLI
- subprocess（Python標準ライブラリ）

## コード例

```
import subprocess, os

def run_claude(prompt: str) -> str:
    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True, text=True, env=env, timeout=300
    )
    return result.stdout.strip()
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
