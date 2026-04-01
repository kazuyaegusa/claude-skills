# Superpowersプラグインをインストールする

> Claude Code公式プラグインマーケットプレイスからSuperpowersをインストールし、エージェントに標準開発ワークフローのスキル群を付与する

- 出典: https://x.com/jiroucaigou/status/2035964407201849564
- 投稿者: 努力赚钱的菜狗
- カテゴリ: claude-code-workflow

## なぜ使うのか

スキルが自動発火するため、ユーザーが何も指示しなくてもエージェントが設計→実装→テスト→レビューのプロセスを守るようになる

## いつ使うのか

Claude CodeまたはCursorで新規プロジェクトを始めるとき、またはAI生成コードのアーキテクチャが崩れ始めたと感じたとき

### 具体的な適用場面

- プロジェクトが大きくなるにつれてAI生成コードの整合性が崩れてきた場合
- Claude CodeやCursorでエージェントに長時間タスクを委任したいが、途中で脱線するのを防ぎたい場合
- チームでAIコーディングを使うが、各自が独自プロセスで動いていて品質がばらつく場合

## やり方

1. Claude Codeの場合: `claude plugin install superpowers` を実行（またはhttps://claude.com/plugins/superpowers からマーケットプレイス経由でインストール）
2. Cursorの場合: Cursorのプラグインマーケットプレイスからインストール
3. Codex/OpenCodeの場合は手動セットアップ: `npx @obra/superpowers install` を実行
4. インストール後はClaude Codeを再起動して有効化を確認

### 入力

- Claude CodeまたはCursorのインストール済み環境
- インターネット接続

### 出力

- TDD・brainstorming・debugging・code review・planning・parallel agents・git worktreesのスキルが自動発火するエージェント環境

## 使うツール・ライブラリ

- claude CLI
- Cursor
- npx @obra/superpowers

## コード例

```
claude plugin install superpowers
# または
npx @obra/superpowers install
```

## 前提知識

- Claude CodeまたはCursorのインストール
- gitの基本操作（branch・worktree）の理解
- TDD（テスト駆動開発）の基本概念

## 根拠

> SuperPowers is a complete software development workflow for your coding agents, built on top of a set of composable 'skills'

> it *doesn't* just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do

> It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY

> it launches a *subagent-driven-development* process, having agents work through each engineering task, inspecting and reviewing their work

> It's not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan
