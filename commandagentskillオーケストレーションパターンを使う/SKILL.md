# Command→Agent→Skillオーケストレーションパターンを使う

> スラッシュコマンド（/xxx）でワークフローを起動し、Agentが隔離コンテキストで実行し、Skillが再利用可能な知識を注入するという3層構造でClaude Codeを運用する

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

役割を分離することでコンテキスト汚染を防ぎ、各層を独立して再利用・更新できるため、複雑なタスクでも品質を保ちやすい

## いつ使うのか

複数ステップにわたる定型ワークフロー（コードレビュー、デプロイ確認、テスト実行など）を繰り返し実行する場合

## やり方

1. `.claude/commands/<name>.md` にワークフロー起動のプロンプトテンプレートを作成
2. `.claude/agents/<name>.md` に特定機能専用のAgentを定義（独自ツール・パーミッション・モデル指定可）
3. `.claude/skills/<name>/SKILL.md` に再利用可能なナレッジ・手順を記述
4. Claude Code上で `claude` 起動後、`/weather-orchestrator` のようにコマンド実行

### 入力

- タスク要件の定義
- 各層のマークダウンファイル

### 出力

- 再利用可能なワークフロー
- 隔離されたAgent実行結果

## 使うツール・ライブラリ

- Claude Code CLI
- .claude/commands/
- .claude/agents/
- .claude/skills/

## コード例

```
# .claude/commands/my-workflow.md
Run the following steps:
1. Use the @analysis-agent to review the code
2. Apply /simplify skill to refactor
3. Commit with a descriptive message
```

## 前提知識

- Claude Code CLIの基本操作（起動、プロンプト入力、コマンド実行）
- GitおよびGitHubの基本知識
- CLAUDE.md、.claude/ディレクトリ構造の理解
- Claude CodeのPlan Mode、Command、Agent、Skillの概念的な区別

## 根拠

> 「公式・コミュニティのClaude Codeベストプラクティスを1箇所にまとめたリポジトリがGitHub月間トレンド入り」

> 「プログラムではなく、情報をまとめたマークダウンがトレンド入りするのがまさに今っぽい。最もレバレッジが効く場所がプログラムではなく、ナレッジになった感」
