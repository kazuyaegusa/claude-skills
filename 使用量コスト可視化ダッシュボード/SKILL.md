# 使用量・コスト可視化ダッシュボード

> Claude Codeのトークン消費量、APIコスト、モデル使用率をリアルタイム集計・グラフ表示する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

サブスクリプション制限に達する前に警告を受け、高コストなモデル（Opus）の過剰使用を防げる

## いつ使うのか

従量課金APIを使用している、またはチームで予算管理が必要な場合

## やり方

1. 使用量モニター（ccflare, better-ccflare, CC Usage等）をインストール
2. ツールが `~/.claude/sessions/` のログを解析し、トークン数・モデル・コストを抽出
3. Webダッシュボード（ccflare）またはCLI（ccusage）で可視化
4. 閾値アラート設定（例: 1日1万トークン超過で通知）
5. 例: ccflareは複数プロバイダ対応（Claude, OpenRouter等）でDocker展開可能

### 入力

- セッション履歴ファイル（.jsonl）
- 料金テーブル（モデルごとのトークン単価）

### 出力

- トークン消費量グラフ（時系列、モデル別）
- 累積コスト
- バーンレート（1時間あたりのトークン消費）

## 使うツール・ライブラリ

- ccflare（Web UI）
- better-ccflare（拡張版）
- CC Usage（CLI）
- Claude Code Usage Monitor（TUI）

## コード例

```
# ccusage 例
ccusage dashboard
# 当日のトークン消費量、コスト、モデル別内訳を表示
```

## 前提知識

- Claude Codeの基本的な使い方（セッション開始、ファイル編集、Bash実行）
- Gitの基礎知識（ブランチ、コミット、PR）
- JSON/YAML形式の理解（設定ファイル記述用）
- （オーケストレータ使用時）Dockerまたはgit worktreeの知識
- （言語特化CLAUDE.md使用時）対象言語のビルドツール知識（pnpm, Gradle, cargo等）

## 根拠

> 「Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.」

> 「Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.」

> 「Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task」

> 「CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards」

> 「ccflare - Claude Code usage dashboard with a web-UI that would put Tableau to shame. Thoroughly comprehensive metrics, frictionless setup, detailed logging, really really nice UI.」
