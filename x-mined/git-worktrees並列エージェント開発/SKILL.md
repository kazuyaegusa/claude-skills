# Git Worktrees並列エージェント開発

> git worktreesを使って複数のエージェントが同一リポジトリの異なるブランチで同時並列に作業できる環境を構築する。tmuxと組み合わせて使う。

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

通常のgit branchでは同一ディレクトリを複数エージェントが触るとコンフリクトが起きるが、worktreesにより各エージェントが独立した作業コピーを持てる。並列開発でスループットが大幅に向上する。

## いつ使うのか

独立した複数機能を同時開発する時、長時間かかるタスクをバックグラウンドで走らせながら別作業をしたい時

### 具体的な適用場面

- Claude Codeを業務・開発に本格導入する際に、Commands/Agents/Skills/Hooksの使い分けを体系的に学びたい場面
- チームでClaude Code運用ルールを標準化し、CLAUDE.mdやサブエージェント設計のベースラインを作りたい場面
- 自分のワークフローを見直してコンテキスト管理・並列開発・プランモードを効果的に活用したい場面

## やり方

1. `git worktree add ../project-feature-a feature-a`で機能ごとに独立したワーキングコピーを作成
2. tmuxで複数ペインを開き、各ペインで異なるworktreeディレクトリに移動
3. 各ペインで`claude`を起動し、独立したタスクを並行実行
4. Claude Code agent teams機能（環境変数で有効化）と組み合わせるとより強力
5. 各ブランチの作業完了後にmainにマージ

### 入力

- gitリポジトリ
- tmuxセットアップ
- 並列化可能なタスク一覧

### 出力

- 独立したブランチで並行する複数の実装
- コンフリクトなしのマージ可能な成果物

## 使うツール・ライブラリ

- git worktree
- tmux
- Claude Code agent teams（beta）

## コード例

```
git worktree add ../project-feature-a feature-a
git worktree add ../project-feature-b feature-b
# tmuxで各ディレクトリにてclaude起動
```

## 前提知識

- Claude Code CLIの基本的な使い方（起動・対話・ファイル操作）
- CLAUDE.md・スラッシュコマンドの概念理解
- gitの基本操作（branch・worktree・commit）

## 根拠

> 「公式・コミュニティのClaude Codeベストプラクティスを1箇所にまとめたリポジトリがGitHub月間トレンド入り」

> 「プログラムではなく、情報をまとめたマークダウンがトレンド入りするのがまさに今っぽい」

> 「最もレバレッジが効く場所がプログラムではなく、ナレッジになった感」

> 「avoid agent dumb zone, do manual /compact at max 50%. Use /clear to reset context mid-session if switching to a new task」

> 「always start with plan mode (Boris)」
