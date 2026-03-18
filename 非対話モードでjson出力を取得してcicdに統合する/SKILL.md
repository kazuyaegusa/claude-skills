# 非対話モードでJSON出力を取得してCI/CDに統合する

> Gemini CLIを`-p`フラグ付きで実行し、`--output-format json`または`stream-json`でAIの応答を構造化データとして取得する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

GitHub ActionsやCron jobなどの自動化パイプラインで、AIエージェントの出力をパース可能な形式で受け取り、後続処理（通知、コミット、デプロイ）に連携できる。

## いつ使うのか

PRマージ前のコードレビュー自動化、Issue自動ラベリング、スケジュールされたコード監査レポート生成など、AIの判断結果を後続プロセスに渡したい場合

## やり方

1. 基本的なテキスト応答: `gemini -p "Explain the architecture"` 2. 構造化JSON応答: `gemini -p "Explain the architecture" --output-format json` 3. ストリーミングイベント（長時間タスク）: `gemini -p "Run tests and deploy" --output-format stream-json | jq ...` 4. GitHub Actionsでの利用例: `google-github-actions/run-gemini-cli`アクションで`prompt`と`output-format`を指定

### 入力

- プロンプト文字列（-pフラグ）
- 出力形式指定（--output-format json|stream-json）
- （オプション）カレントディレクトリのコードベース

### 出力

- JSON形式のAI応答（エラーハンドリング用のstatusフィールド含む）
- stream-json形式のリアルタイムイベントストリーム

## 使うツール・ライブラリ

- gemini-cli
- jq（JSONパース）
- google-github-actions/run-gemini-cli

## コード例

```
# GitHub Actions workflow例
- uses: google-github-actions/run-gemini-cli@v1
  with:
    prompt: 'Review this PR and suggest improvements'
    output-format: json
- run: |
    echo "${{ steps.gemini.outputs.response }}" | jq '.suggestions'
```

## 前提知識

- Node.js環境の基本操作（npmまたはnpxの使用経験）
- ターミナル/コマンドラインの基礎知識
- Git操作の基本（GitHub連携を使う場合）
- JSON-RPC 2.0の基礎（MCP Server自作時）
- Google Cloud Projectの概念（Code Assistライセンス利用時）
- CI/CDパイプラインの基礎（GitHub Actions統合時）

## 根拠

> 「Free tier: 60 requests/min and 1,000 requests/day with personal Google account」（OAuth認証での無料枠）

> 「Powerful Gemini 3 models: Access to improved reasoning and 1M token context window」（モデル性能）

> 「Run non-interactively in scripts for workflow automation」「--output-format json」「--output-format stream-json」（非対話モード）

> 「Custom context files (GEMINI.md) to tailor behavior for your projects」（コンテキストファイル）

> 「Conversation checkpointing to save and resume complex sessions」（チェックポイント機能）
