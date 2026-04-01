# 構造化出力をパイプラインに組み込む

> claude --json-schemaの出力を他のコマンドやスクリプトにパイプで渡し、ワークフロー全体を自動化する

- 出典: https://x.com/suna_gaku/status/2014661966875570417
- 投稿者: スナガク
- カテゴリ: claude-code-workflow

## なぜ使うのか

構造化出力が保証されることで、Claude Codeを単独ツールではなくパイプラインの1部品として扱えるようになり、複雑な自動化が可能になる

## いつ使うのか

Claude Codeの判断結果を元に後続処理を分岐させたい時、複数ツールを組み合わせた自動化フローを構築したい時

### 具体的な適用場面

- Claude Codeの出力を他のツール（jq、Python、シェルスクリプト）で加工したい時
- CI/CDパイプラインでコード分析結果を構造化データとして取得したい時
- 複数のClaude Code実行結果を集約・比較したい時
- Claude Codeの出力をデータベースやAPIに自動送信したい時

## やり方

1. スキーマを定義（例: {"type": "object", "properties": {"tasks": {"type": "array"}}}） 2. claude -p "..." --json-schema schema.json | jq -r '.tasks[]' | xargs -I {} sh -c 'process {}' のようにパイプラインを構築 3. 各工程で構造化データを前提とした処理を実装

### 入力

- パイプライン全体の入力（コードベース、設定ファイル等）
- 各ステップのJSONスキーマ

### 出力

- パイプライン全体の最終成果物（レポート、通知、自動コミット等）

## 使うツール・ライブラリ

- claude CLI
- jq
- xargs
- シェルスクリプト

## コード例

```
claude -p "$(cat task.md)" --json-schema output.schema.json | jq -r '.actions[]' | parallel --jobs 4 'claude -p "Execute: {}" --json-schema result.schema.json'
```

## 前提知識

- Claude Code CLIの基本的な使い方（claude -p でプロンプト実行）
- JSONスキーマの基本構文（type, properties, required等）
- jqやシェルスクリプトでのJSON操作（パイプライン構築する場合）

## 根拠

> 「--json-schema オプションで形式を指定すると、指定した JSON 形式で出力してくれる」

> 「JSON 形式で出力できればワークフローの自動化やパイプライン構築に便利」

> 画像に claude -p "..." --json-schema schema.json の実行例が表示されている
