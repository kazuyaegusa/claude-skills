# AskUserQuestionツールでインタビュー形式の仕様収集をする

> Claude Codeに `AskUserQuestion` ツールを使ったインタビュー形式で仕様を引き出させ、その後新セッションで実装を実行する

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

最初から詳細仕様を書くのは難しい。ClaudeをインタビュアーにすることでYagni/あいまいさを事前排除でき、実装品質が向上する

## いつ使うのか

何を作るかはわかっているが詳細要件が曖昧な場合、プロトタイプ前のスペック作成時

## やり方

1. 「AskUserQuestionツールを使って、実装に必要な情報を私にインタビューしてください」と指示
2. Claudeが不明点を質問してくる → 回答する
3. インタビュー完了後、Claudeが仕様をまとめる
4. その仕様を持って `/clear` または新セッションで実装開始

### 入力

- 作りたいものの大まかなアイデア

### 出力

- 明確化された仕様書
- 実装に必要な前提条件リスト

## 使うツール・ライブラリ

- AskUserQuestion（Claude Code内蔵ツール）

## コード例

```
AskUserQuestionツールを使って実装前に私にインタビューし、仕様を明確化してください
```

## 前提知識

- Claude Code CLIの基本操作（起動、プロンプト入力、コマンド実行）
- GitおよびGitHubの基本知識
- CLAUDE.md、.claude/ディレクトリ構造の理解
- Claude CodeのPlan Mode、Command、Agent、Skillの概念的な区別

## 根拠

> 「公式・コミュニティのClaude Codeベストプラクティスを1箇所にまとめたリポジトリがGitHub月間トレンド入り」

> "CLAUDE.md should target under 200 lines per file"

> "use Esc Esc or /rewind to undo when Claude goes off-track instead of trying to fix it in the same context"
