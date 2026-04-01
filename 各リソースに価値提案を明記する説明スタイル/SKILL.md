# 各リソースに"価値提案"を明記する説明スタイル

> 単なる機能説明ではなく、そのリソースが解決する問題や提供する価値を明確に記述する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

ユーザーは「これが何か」よりも「これが自分にとって何をしてくれるか」を知りたい。価値提案を明示することで、導入判断を迅速化できる

## いつ使うのか

ツールやリソースのキュレーションで、読者の導入判断を支援したい場合

## やり方

1. リソース名とリンクを記載
2. 作者名とリンクを記載
3. 1-3文で以下を含む説明を記述：
   - 主要機能（何をするか）
   - 解決する問題（なぜ必要か）
   - 特徴的な機能や差別化要素
4. 技術的詳細よりもユースケースを重視
5. 必要に応じて注記（NOTE）で開発状況や注意点を追加

### 入力

- リソースのREADMEや説明文
- 実際の使用経験（可能であれば）

### 出力

- 価値提案を含む簡潔な説明文（1-3文）

## コード例

```
- [agnix](https://github.com/agent-sh/agnix) by [agent-sh](https://github.com/agent-sh) - A comprehensive linter for Claude Code agent files. Validate CLAUDE.md, AGENTS.md, SKILL.md, hooks, MCP, and more. Plugin for all major IDEs included, with auto-fixes.
```

## 前提知識

- Claude Codeの基本的な使い方（CLI、設定ファイル、コマンド実行）
- GitHubの基本操作（リポジトリのクローン、READMEの閲覧）
- Markdownの読解
- AI開発ツールの一般的な概念（エージェント、フック、プロンプト等）
