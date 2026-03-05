---
name: Ticket-to-PR Pipeline
version: 1.0.0
description: プロジェクト管理チケットからAIコード生成→GitHub PR作成を自動化するオーケストレーションパターン
author: extracted-from-symphony
tags: [automation, ai-coding, pipeline, linear, github, openai]
---

# Ticket-to-PR Pipeline

プロジェクト管理ツール（Linear等）のチケットを入力として、AI でコード生成し、GitHub に PR を自動作成するパイプライン。

## アーキテクチャ

```
チケット作成/更新 → Webhook受信 → AI コード生成 → GitHub ブランチ+コミット → PR作成 → チケットにコメント
```

## 依存パッケージ

```
httpx
openai
aiohttp
```

## 環境変数

- `LINEAR_API_KEY` — Linear API キー
- `OPENAI_API_KEY` — OpenAI API キー
- `GITHUB_TOKEN` — GitHub Personal Access Token
- `GITHUB_REPO` — 対象リポジトリ `owner/repo`
- `LINEAR_WEBHOOK_SECRET` — Webhook 署名検証用（任意）
- `WEBHOOK_PORT` — サーバーポート（デフォルト: 8000）
- `CODEX_MODEL` — 使用モデル（デフォルト: o4-mini）

## 使い方

### Webhook サーバーモード

```bash
python main.py
```

Linear の Webhook URL に `http://your-server:8000/webhook/linear` を設定。
"symphony" ラベル付きチケットが作成/更新されるとパイプラインが起動。

### 単発実行モード

```bash
python main.py <linear-issue-id>
```

指定した Issue ID のチケットに対してパイプラインを1回実行。

## カスタマイズポイント

- `CodeGenerator` クラスを差し替えれば OpenAI 以外の LLM も利用可能
- `Orchestrator.handle_issue()` のフローを変更すればテスト実行やレビュー依頼も追加可能
- Webhook のトリガー条件（ラベル名等）は `webhook_server.py` で変更

## パイプラインフロー詳細

1. **チケット取得**: Linear API で Issue の title/description/labels を取得
2. **ブランチ名生成**: `pipeline/{identifier}-{slug}` 形式で自動生成
3. **AI コード生成**: チケット情報を LLM に渡し、ファイル変更を JSON で受け取る
4. **GitHub 操作**: ブランチ作成 → ファイルコミット → PR 作成
5. **フィードバック**: Linear チケットに PR URL をコメント

## 注意事項

- API キーは `os.getenv()` で取得（ハードコード禁止）
- Webhook 署名検証は本番環境では必ず有効にすること
- LLM のコード生成結果は必ずレビューすること（自動マージは推奨しない）
