# 非インタラクティブモード（headless）でのスクリプト実行

> `-p` フラグでプロンプトを渡し、Gemini CLIを非対話モードで実行し、JSON出力を得る

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

CI/CD、cron、自動化スクリプトに組み込むため

## いつ使うのか

自動テスト生成、定期レポート生成、CI/CDパイプライン組み込み時

## やり方

1. `gemini -p "プロンプト" --output-format json` を実行
2. 構造化されたJSON応答を受け取る
3. jqやPython等でパース・後続処理
4. リアルタイム監視が必要な場合は `--output-format stream-json` を使用

### 入力

- プロンプト文字列
- （任意）--output-format フラグ

### 出力

- JSON形式の応答またはストリームJSON

## 使うツール・ライブラリ

- gemini CLI
- jq（JSON処理）

## コード例

```
gemini -p "Explain the architecture of this codebase" --output-format json
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Google アカウント（OAuth認証用）
- （任意）Gemini API Key または Vertex AI認証情報
- （GitHub Action利用時）GitHub リポジトリ管理権限
- （MCP利用時）各MCPサーバーのセットアップ知識
