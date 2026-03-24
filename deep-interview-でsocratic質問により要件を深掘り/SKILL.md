# /deep-interview でSocratic質問により要件を深掘り

> 曖昧なアイデアをSocratic法（問答法）で段階的に掘り下げ、隠れた前提・制約・ゴールを言語化してから実装に入る

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

「なんとなく作りたい」状態でコードを書き始めると、途中で方向転換・手戻りが発生しコストが増大する。deep-interviewは実装前に要件を多次元（技術/UX/制約/成功指標）で評価し、明確化してから作業開始するため手戻りゼロ

## いつ使うのか

プロジェクト開始時に「何を作るか」が曖昧な場合、ステークホルダーが複数いて要件がブレやすい場合、過去に手戻りが多発した経験がある場合

## やり方

1. `/deep-interview "vague idea"` でインタビュー開始
2. oh-my-claudecodeが Socratic 質問を連続投下（「誰が使う？」「成功とは？」「既存ツールとの違いは？」）
3. 回答するごとに clarity score が重み付き次元で計算される
4. 全次元で閾値を超えたら要件定義完了、実装フェーズへ移行
5. 未達の場合はさらに深掘り質問が追加される

### 入力

- 曖昧なアイデア・プロジェクト構想の1文

### 出力

- 多次元で評価された要件明確度スコア
- 実装可能レベルまで具体化された要件定義
- 次のアクションプラン

## 使うツール・ライブラリ

- oh-my-claudecode deep-interview skill

## コード例

```
/deep-interview "I want to build a task management app"

# 以下のような質問が自動で投げられる:
# - Who are the primary users?
# - What does success look like?
# - What existing tools does this replace?
# - What are the top 3 constraints (time/budget/tech)?
# - How will you measure adoption?
```

## 前提知識

- Claude Code CLI インストール済み
- Claude Max/Pro サブスクリプション または Anthropic API キー
- tmux インストール（macOS: brew install tmux / Ubuntu: apt install tmux / Windows: psmux）
- 基本的なコマンドライン操作知識
- YAML/JSON設定ファイルの読み書き
- （オプション）codex CLI / gemini CLI（異種LLM統合を使う場合）

## 根拠

> 「The deep interview uses Socratic questioning to clarify your thinking before any code is written」
