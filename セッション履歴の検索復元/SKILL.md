# セッション履歴の検索・復元

> 過去のClaude Codeセッションログ（.jsonl）を全文検索し、関連する会話・コード変更を復元する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeはセッション間でコンテキストを持たないため、過去の議論や決定事項を再利用するには手動で履歴を掘り起こす必要があるが、検索ツールで自動化できる

## いつ使うのか

過去に似た問題を解決した記憶があるが、いつのセッションか思い出せない時、または長期プロジェクトで数ヶ月前の設計判断を参照したい時

## やり方

1. セッション検索ツール（recall, claude-code-tools, Claudex等）をインストール
2. ツールが `~/.claude/sessions/` 配下の全.jsonlファイルをインデックス化
3. キーワード検索（例: `recall "TDD implementation"`）で関連セッションを抽出
4. 見つかったセッションを `claude --resume <session-id>` で復元、または要約を取得
5. 例: claude-code-toolsはRust/Tantivyベースで2GB超のログも高速検索

### 入力

- 検索キーワード
- セッション履歴ファイル（.jsonl）

### 出力

- マッチしたセッションのリスト（タイムスタンプ、要約付き）
- 復元可能なセッションID

## 使うツール・ライブラリ

- recall（シンプルCLI）
- claude-code-tools（Rust製高速検索）
- Claudex（Webブラウザ + 全文検索）

## コード例

```
# recall 使用例
recall "authentication JWT"
# マッチしたセッションが表示され、Enterで復元
```

## 前提知識

- Claude Codeの基本的な使い方（セッション開始、ファイル編集、Bash実行）
- Gitの基礎知識（ブランチ、コミット、PR）
- JSON/YAML形式の理解（設定ファイル記述用）
- （オーケストレータ使用時）Dockerまたはgit worktreeの知識
- （言語特化CLAUDE.md使用時）対象言語のビルドツール知識（pnpm, Gradle, cargo等）

## 根拠

> 「recall - Full-text search your Claude Code sessions. Run `recall` in terminal, type to search, Enter to resume.」
