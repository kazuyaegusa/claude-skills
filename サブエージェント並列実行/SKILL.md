# サブエージェント並列実行

> 親エージェントから独立したサブエージェントを並列起動し、Pythonスクリプト経由でツールRPC呼び出し

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

複数ワークストリームを並列処理すると速度向上。また、複雑なパイプライン（スクレイピング→加工→保存）をPythonスクリプトに閉じ込めれば、LLMコンテキストを消費せずマルチステップ処理可能

## いつ使うのか

データ収集と分析を並列実行したい、または複雑なツール連鎖をLLMコンテキスト外で自動化したい場合

## やり方

1. 親エージェントから spawn_subagent(task_description) で子起動
2. サブエージェントは独立した会話コンテキスト
3. Pythonスクリプト内でRPC経由でツール呼び出し（例: execute_bash, read_file等）
4. 結果を親エージェントに統合

### 入力

- サブタスク定義
- Pythonスクリプト（RPC呼び出し）

### 出力

- 並列実行結果
- コンテキストコスト削減

## 使うツール・ライブラリ

- asyncio（並列実行）
- RPC機構（詳細未明記）

## コード例

```
# サブエージェント起動例（conceptual）
subagent = agent.spawn_subagent('Scrape competitor pricing')
# Pythonスクリプトでツール呼び出し例
import hermes_rpc
data = hermes_rpc.call('web_scraper', url='https://...')
hermes_rpc.call('write_file', path='data.json', content=json.dumps(data))
```

## 前提知識

- Linux/macOS/WSL2環境（Windowsネイティブ非対応）
- gitインストール済み
- AIエージェント・LLM基礎知識（tool calling, context window等）
- ターミナル操作の基本（bash, curl等）
- 各メッセージングプラットフォームのBot API取得方法（Telegram/Discord等）
- （サーバーレス利用時）Daytona/ModalアカウントとAPI認証
- （LLM利用）OpenRouter/OpenAI等のAPIキー
