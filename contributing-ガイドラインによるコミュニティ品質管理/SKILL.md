# Contributing ガイドラインによるコミュニティ品質管理

> リソース推薦のプロセスを自動化し、PRではなくIssueテンプレート経由での投稿を強制することで、品質基準を維持する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

オープンソースプロジェクトでは、低品質な投稿やスパムが問題になりやすい。標準化されたフォームと明確なガイドラインにより、一貫した品質を保ちながらコミュニティ貢献を促進できる

## いつ使うのか

コミュニティ主導のキュレーションプロジェクトで、品質管理とスケーラビリティを両立したい場合

## やり方

1. CONTRIBUTING.md と CODE_OF_CONDUCT.md を作成
2. GitHubのIssueテンプレート（recommend-resource.yml等）を設定
3. READMEに"Recommend a new resource here!"リンクを配置
4. "the only person who is allowed to submit PRs to this repo is Claude"と明記し、PRを受け付けない方針を明示
5. 投稿された推薦を人間（または自動化されたClaude）がレビュー・統合

### 入力

- Issueテンプレート定義
- 品質基準・ガイドライン

### 出力

- 標準化されたリソース推薦プロセス
- 一貫性のあるリソース品質

## 使うツール・ライブラリ

- GitHub Issues
- Issue Templates
- GitHub Actions（推測）

## コード例

```
## Contributing

### **[Recommend a new resource here!](https://github.com/hesreallyhim/awesome-claude-code/issues/new?template=recommend-resource.yml)**

...Please do not open a PR to submit a recommendation - the only person who is allowed to submit PRs to this repo is Claude.
```

## 前提知識

- Claude Codeの基本的な使い方（CLI、設定ファイル、コマンド実行）
- GitHubの基本操作（リポジトリのクローン、READMEの閲覧）
- Markdownの読解
- AI開発ツールの一般的な概念（エージェント、フック、プロンプト等）

## 根拠

> "Agent Skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks" - カテゴリー定義の例

> "Please do not open a PR to submit a recommendation - the only person who is allowed to submit PRs to this repo is Claude" - 品質管理方針
