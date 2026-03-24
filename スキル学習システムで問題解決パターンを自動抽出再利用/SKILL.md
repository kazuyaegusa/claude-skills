# スキル学習システムで問題解決パターンを自動抽出・再利用

> セッション中の対話から「再利用可能な問題解決パターン」を自動抽出してYAML形式のスキルファイル化し、次回以降同じtriggerに遭遇したら自動でコンテキストに注入する

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

同じバグ・設定問題に何度も遭遇するとき、毎回ゼロから調査・修正するのは非効率。一度解決した知識をスキル化すれば、triggerキーワードで自動呼び出しされ即座に対処できる

## いつ使うのか

難解なバグを解決した直後、特定ライブラリのハマりどころを克服した時、チーム共通の設定手順を標準化したい時

## やり方

1. `/learner` コマンドで現セッションから学習実行
2. oh-my-claudecodeが会話履歴を分析し、再利用価値のあるパターンを検出
3. `.omc/skills/` (プロジェクト) または `~/.omc/skills/` (ユーザー全体) にYAMLファイル生成
4. 次回以降、promptに trigger キーワードが含まれると自動でスキル内容がコンテキストに注入
5. `/skill list | add | remove | edit | search` でスキル管理

### 入力

- 解決済みのセッション履歴
- スキル化したい問題のtriggerキーワード

### 出力

- .omc/skills/*.md (プロジェクトスコープ) または ~/.omc/skills/*.md (ユーザースコープ)
- YAML front-matter付きMarkdownファイル（name, description, triggers, source）

## 使うツール・ライブラリ

- oh-my-claudecode Learner機能
- /learner, /skill コマンド

## コード例

```
# スキルファイル例: .omc/skills/fix-proxy-crash.md
---
name: Fix Proxy Crash
description: aiohttp proxy crashes on ClientDisconnectedError
triggers: ["proxy", "aiohttp", "disconnected"]
source: extracted
---
Wrap handler at server.py:42 in try/except ClientDisconnectedError...

# スキル管理コマンド
/skill list
/skill add <name>
/skill remove <name>
/skill search <keyword>
```

## 前提知識

- Claude Code CLI インストール済み
- Claude Max/Pro サブスクリプション または Anthropic API キー
- tmux インストール（macOS: brew install tmux / Ubuntu: apt install tmux / Windows: psmux）
- 基本的なコマンドライン操作知識
- YAML/JSON設定ファイルの読み書き
- （オプション）codex CLI / gemini CLI（異種LLM統合を使う場合）

## 根拠

> 「v4.4.0 removes the Codex/Gemini MCP servers (x, g providers). Use the CLI-first Team runtime (omc team ...) to spawn real tmux worker panes」
