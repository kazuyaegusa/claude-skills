# Skillシステムで過去の知見を自動再利用

> プロジェクト固有（.omc/skills/）またはユーザー全体（~/.omc/skills/）のデバッグ知識をYAML形式で保存し、関連タスク時に自動注入する

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

一度解決した問題を毎回再調査するのは非効率。Skillとして保存すれば、triggersキーワードに合致時に自動的にコンテキスト注入され即座に解決できる

## いつ使うのか

繰り返し発生するバグ、プロジェクト固有の設定トラブル、チーム内で共有すべき解決策がある時

## やり方

1. `.omc/skills/fix-proxy-crash.md` のようなファイルを作成
2. YAMLフロントマターで name/description/triggers/source を定義
3. 本文に具体的な修正手順を記述
4. `/skill add <path>` で登録（または手動配置）
5. 該当キーワードを含むタスク時に自動ロード
6. `/learner` で既存セッションから自動抽出も可能

### 入力

- 過去のデバッグ経験・解決策
- トリガーキーワードの定義

### 出力

- .omc/skills/*.md ファイル（version control可能）
- ~/.omc/skills/*.md ファイル（全プロジェクトで共有）
- 関連タスク時の自動コンテキスト注入

## 使うツール・ライブラリ

- oh-my-claudecode
- YAML frontmatter

## コード例

```
# .omc/skills/fix-proxy-crash.md
---
name: Fix Proxy Crash
description: aiohttp proxy crashes on ClientDisconnectedError
triggers: ["proxy", "aiohttp", "disconnected"]
source: extracted
---
Wrap handler at server.py:42 in try/except ClientDisconnectedError...
```

## 前提知識

- Claude Code CLIの基本操作（インストール・起動）
- Claude Max/ProサブスクリプションまたはAnthropic APIキー
- tmux（CLI workers使用時）
- Node.js/npm（プラグインインストール時）
- Git（スキルのバージョン管理時）
