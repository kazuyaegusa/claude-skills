# CLAUDE.mdを200行以内に管理する

> プロジェクトルートのCLAUDE.mdは200行以下に保ち、大きくなったら `.claude/rules/` 配下のファイルに分割する

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

CLAUDE.mdはコンテキストに常時ロードされるため、長すぎると後半が無視されやすくなる。Borisが推奨する上限は200行

## いつ使うのか

CLAUDE.mdが肥大化してClaudeが指示を無視するようになった時、またはモノレポでサブプロジェクト別の指示が必要な時

## やり方

1. CLAUDE.mdの行数を定期確認（`wc -l CLAUDE.md`）
2. 200行を超えたら機能カテゴリ別に分割（例: `.claude/rules/testing.md`, `.claude/rules/git.md`）
3. モノレポの場合は各サブディレクトリにも個別CLAUDE.mdを配置（祖先→子孫の順にロードされる）
4. `@path` インポート構文で外部ファイルを参照

### 入力

- 既存のCLAUDE.md

### 出力

- 200行以内のCLAUDE.md
- カテゴリ別の.claude/rules/ファイル群

## 使うツール・ライブラリ

- Claude Code Memory機能

## コード例

```
# CLAUDE.md
@.claude/rules/testing.md
@.claude/rules/git-workflow.md

## Core Rules
...
```

## 前提知識

- Claude Code CLIの基本操作（起動、プロンプト入力、コマンド実行）
- GitおよびGitHubの基本知識
- CLAUDE.md、.claude/ディレクトリ構造の理解
- Claude CodeのPlan Mode、Command、Agent、Skillの概念的な区別

## 根拠

> 「公式・コミュニティのClaude Codeベストプラクティスを1箇所にまとめたリポジトリがGitHub月間トレンド入り」

> 「プログラムではなく、情報をまとめたマークダウンがトレンド入りするのがまさに今っぽい。最もレバレッジが効く場所がプログラムではなく、ナレッジになった感」
