# 「エレガントな解法」プロンプトで品質を強制する

> 平凡な修正が出た後に「knowing everything you know now, scrap this and implement the elegant solution」と指示し、最適解を引き出す

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claudeは最初に「動く解」を出すことを優先しがちで、最適解を出さないことがある。明示的に「最初からやり直し」を命じることでより良いアーキテクチャの解が得られる

## いつ使うのか

最初の実装が動くが品質が低い場合、技術的負債になりそうなコードが出た場合

## やり方

1. Claudeが最初の実装を出す
2. 結果が動くが冗長・複雑と判断した場合
3. `knowing everything you know now, scrap this and implement the elegant solution` と入力
4. または「証明してみせろ」系: `prove to me this works` `grill me on these changes` でClaudeに自己検証させる

### 入力

- Claudeが生成した初回実装

### 出力

- よりシンプル・エレガントなリファクタ済み実装

## コード例

```
knowing everything you know now, scrap this and implement the elegant solution
```

## 前提知識

- Claude Code CLIの基本操作（起動、プロンプト入力、コマンド実行）
- GitおよびGitHubの基本知識
- CLAUDE.md、.claude/ディレクトリ構造の理解
- Claude CodeのPlan Mode、Command、Agent、Skillの概念的な区別

## 根拠

> "knowing everything you know now, scrap this and implement the elegant solution" (Boris Cherny)

> "use Esc Esc or /rewind to undo when Claude goes off-track instead of trying to fix it in the same context"

> "agent teams with tmux and git worktrees for parallel development"
