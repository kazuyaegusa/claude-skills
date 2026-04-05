# publish.shによるスキル配布とプロジェクト初期化

> スキル開発リポジトリから新規ゲームプロジェクトフォルダへスキル一式をコピーし、git初期化まで自動実行

- 出典: https://github.com/htdt/godogen
- 投稿者: htdt
- カテゴリ: claude-code-workflow

## なぜ使うのか

スキル開発環境とゲーム制作環境を分離し、ユーザーが即座にゲーム制作を開始できるようにするため

## いつ使うのか

Claude Code Skillsの配布・インストールを簡略化したい場合、テンプレートプロジェクトをユーザーに提供したい場合

## やり方

1. `./publish.sh ~/my-game` 実行
2. ターゲットディレクトリに `.claude/skills/` と `CLAUDE.md` を配置
3. git init 実行
4. Claude Codeでそのフォルダを開き `/godogen` スキルでゲーム記述を入力

### 入力

- スキル開発リポジトリ
- ターゲットディレクトリパス

### 出力

- 即座に使えるゲームプロジェクトフォルダ（スキル・設定・git初期化済み）

## 使うツール・ライブラリ

- bash
- git

## コード例

```
#!/bin/bash
# publish.sh
target="$1"
[[ "$2" == "--force" ]] && rm -rf "$target"
mkdir -p "$target/.claude/skills"
cp -r skills/* "$target/.claude/skills/"
cp CLAUDE.md "$target/"
cd "$target" && git init
```

## 前提知識

- Claude Codeの基本的な使い方とSkills機能の理解
- Godot 4の基礎知識（シーン、ノード、GDScriptの概念）
- API利用のための環境変数設定（GOOGLE_API_KEY, XAI_API_KEY, TRIPO3D_API_KEY）
- Linux/macOSのコマンドライン操作（依存パッケージインストール）
- LLMの文脈窓とトークン制限の理解
- （推奨）GCE等クラウドVM利用経験（長時間実行・GPU利用の場合）

## 根拠

> 「Three Claude Code skills — one orchestrator runs the full pipeline in a single 1M-token context window (planning, building, debugging), while two forked support skills handle Godot API lookup and visual QA without polluting the main context.」

> 「Visual QA closes the loop — captures actual screenshots from the running game and analyzes them with Gemini Flash and Claude vision. Includes question mode for free-form visual debugging. Catches z-fighting, missing textures, broken physics.」

> 「./publish.sh ~/my-game ... This creates the target directory with `.claude/skills/` and a `CLAUDE.md`, then initializes a git repo.」

> 「2026-04-03 — Single-context architecture (current) - Merged task executor into godogen — full pipeline runs in one 1M-token context window - Added godot-api skill (forked, Sonnet) for Godot class API lookup - Added visual-qa skill (forked) with Gemini Flash, Claude vision, and question mode - Risk-first decomposition replaces task DAG」
