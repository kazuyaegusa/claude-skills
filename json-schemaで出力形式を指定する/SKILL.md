# --json-schemaで出力形式を指定する

> Claude Code CLI実行時に--json-schemaオプションでJSONスキーマファイルを指定し、そのスキーマに従ったJSON形式で出力させる

- 出典: https://x.com/suna_gaku/status/2014661966875570417
- 投稿者: スナガク
- カテゴリ: claude-code-workflow

## なぜ使うのか

自由形式のテキスト出力はパースが不安定で自動化に向かない。スキーマ指定により確実に期待した構造のデータを取得でき、後続処理が安定する

## いつ使うのか

Claude Codeの出力を機械的に処理したい時、複数の実行結果を統一フォーマットで集めたい時

### 具体的な適用場面

- Claude Codeの出力を他のツール（jq、Python、シェルスクリプト）で加工したい時
- CI/CDパイプラインでコード分析結果を構造化データとして取得したい時
- 複数のClaude Code実行結果を集約・比較したい時
- Claude Codeの出力をデータベースやAPIに自動送信したい時

## やり方

1. 期待する出力のJSONスキーマをファイル（例: schema.json）として用意する 2. claude -p "タスク内容" --json-schema schema.json を実行 3. 標準出力に指定したスキーマに従ったJSONが出力される 4. jqやPythonでパースして後続処理に渡す

### 入力

- Claude Codeに実行させたいプロンプト
- 期待する出力構造を定義したJSONスキーマファイル

### 出力

- 指定したスキーマに準拠したJSON文字列

## 使うツール・ライブラリ

- claude CLI
- jq（JSON加工用、任意）

## コード例

```
claude -p "コードレビューして問題点をリストアップ" --json-schema review_schema.json | jq '.issues[]'
```

## 前提知識

- Claude Code CLIの基本的な使い方（claude -p でプロンプト実行）
- JSONスキーマの基本構文（type, properties, required等）
- jqやシェルスクリプトでのJSON操作（パイプライン構築する場合）

## 根拠

> 「--json-schema オプションで形式を指定すると、指定した JSON 形式で出力してくれる」

> 「JSON 形式で出力できればワークフローの自動化やパイプライン構築に便利」

> 画像に claude -p "..." --json-schema schema.json の実行例が表示されている
