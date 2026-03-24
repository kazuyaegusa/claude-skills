# GEMINI.mdでプロジェクト固有コンテキストを永続化

> プロジェクトルートに`GEMINI.md`を配置し、Gemini CLIにコーディング規約・アーキテクチャ情報を常に読み込ませる

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: context-management

## なぜ使うのか

毎回同じ前提を説明する手間を省き、プロジェクト特有のルールに沿った回答を得られるため

## いつ使うのか

複数人でプロジェクトを開発し、AI生成コードに一貫性を持たせたい場合

## やり方

1. プロジェクトルートに`GEMINI.md`ファイルを作成
2. コーディング規約、使用技術スタック、アーキテクチャ概要、禁止事項などを記述
3. Gemini CLIを起動すると自動的に読み込まれる
4. チーム全体でリポジトリにcommitして共有

### 入力

- プロジェクト固有の規約・前提知識

### 出力

- Gemini CLIが常にコンテキストを把握した状態で応答

## 使うツール・ライブラリ

- GEMINI.md（プレーンテキスト）

## コード例

```
# GEMINI.md
## Coding Rules
- Use TypeScript strict mode
- Prefer functional components
## Architecture
- MVC pattern with services layer
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Googleアカウント（OAuth認証用）
- ターミナル操作の基礎知識
- （GitHub連携時）GitHubリポジトリとActions実行権限
- （MCP統合時）各サービスのAPI認証情報

## 根拠

> 🧠 Powerful Gemini 3 models: Access to improved reasoning and 1M token context window.

> npx @google/gemini-cli

> gemini -p "Explain the architecture of this codebase" --output-format json

> Custom context files (GEMINI.md) to tailor behavior for your projects

> Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action
