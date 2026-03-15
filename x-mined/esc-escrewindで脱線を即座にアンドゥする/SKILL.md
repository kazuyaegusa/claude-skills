# Esc Esc（/rewind）で脱線を即座にアンドゥする

> Claudeが間違った方向に進んだ時、同じコンテキストで修正しようとせず `Esc Esc` または `/rewind` で直前の状態にロールバックする

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

コンテキスト内で「修正の修正」を積み重ねると複雑化し、より悪い状態になることが多い。Checkpointing機能でgitベースのundo/rewindが可能

## いつ使うのか

Claudeが間違ったアプローチで実装を進め始めた時。「修正するより最初からやり直す方が早い」と判断した時

## やり方

1. Claudeが意図と異なる実装を始めたと気づいた時点で即座に `Esc` を押して停止
2. `Esc Esc` または `/rewind` でファイル変更をロールバック
3. より明確な指示を与えて再実行
4. または `/clear` で完全リセット後、仕様を明確化して再開

### 入力

- 脱線したClaudeセッション

### 出力

- ロールバックされたファイル状態
- クリーンな再実行環境

## 使うツール・ライブラリ

- /rewind
- Checkpointing機能（git-based）

## 前提知識

- Claude Code CLIの基本操作（起動、プロンプト入力、コマンド実行）
- GitおよびGitHubの基本知識
- CLAUDE.md、.claude/ディレクトリ構造の理解
- Claude CodeのPlan Mode、Command、Agent、Skillの概念的な区別

## 根拠

> "use Esc Esc or /rewind to undo when Claude goes off-track instead of trying to fix it in the same context"
