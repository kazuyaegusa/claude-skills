# GEMINI.mdによるプロジェクト固有文脈の永続化

> プロジェクトルートに `GEMINI.md` を配置し、常に参照される文脈・ルール・ガイドラインを記述する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

セッションごとに同じ指示を繰り返さず、チーム全体で一貫した動作を保証するため

## いつ使うのか

チーム開発、複数人での一貫性確保、プロジェクト固有ルールの強制時

## やり方

1. プロジェクトルートに `GEMINI.md` を作成
2. コーディング規約、アーキテクチャ方針、禁止事項等を記述
3. Gemini CLI起動時に自動読み込み
4. 全プロンプトでこの文脈が参照される

### 入力

- GEMINI.md ファイル

### 出力

- 文脈を反映したGemini CLIの振る舞い

## 使うツール・ライブラリ

- Gemini CLI

## コード例

```
# GEMINI.md の例
## Coding Rules
- Use TypeScript strict mode
- Prefer immutable data structures
- All functions must have unit tests
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Google アカウント（OAuth認証用）
- （任意）Gemini API Key または Vertex AI認証情報
- （GitHub Action利用時）GitHub リポジトリ管理権限
- （MCP利用時）各MCPサーバーのセットアップ知識

## 根拠

> "Powerful Gemini 3 models: Access to improved reasoning and 1M token context window."

> "npx @google/gemini-cli" - インストール不要実行

> "Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action"

> "Custom context files (GEMINI.md) to tailor behavior for your projects"
