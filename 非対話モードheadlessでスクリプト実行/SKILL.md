# 非対話モード（headless）でスクリプト実行

> 対話セッションを開かず、`-p`フラグで直接プロンプトを渡して結果を取得する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: prompt-engineering

## なぜ使うのか

CI/CDパイプラインやシェルスクリプトでGemini CLIを組み込むため

## いつ使うのか

自動化スクリプト、GitHub Actions、デプロイパイプラインでAI判断を組み込みたい場合

## やり方

1. テキスト応答の場合: `gemini -p "質問文"`
2. JSON形式で構造化出力が必要な場合: `gemini -p "質問文" --output-format json`
3. リアルタイムイベントストリーミングの場合: `gemini -p "質問文" --output-format stream-json`
4. 標準出力をパースして後続処理に渡す

### 入力

- プロンプト文字列
- （オプション）出力フォーマット指定（json, stream-json）

### 出力

- テキスト応答またはJSON形式の構造化データ

## 使うツール・ライブラリ

- gemini CLI
- jqなどのJSONパーサー（スクリプト連携時）

## コード例

```
gemini -p "Explain the architecture of this codebase" --output-format json
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Googleアカウント（OAuth認証用）
- ターミナル操作の基礎知識
- （GitHub連携時）GitHubリポジトリとActions実行権限
- （MCP統合時）各サービスのAPI認証情報

## 根拠

> gemini -p "Explain the architecture of this codebase" --output-format json
