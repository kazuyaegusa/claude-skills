# Command→Agent→Skillオーケストレーション

> Claude Codeの3つの拡張機能（Commands・Subagents・Skills）を役割分担して組み合わせ、複雑なワークフローを自動化するアーキテクチャパターン。

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一のClaudeセッションでは対応しにくい複雑なタスクを、役割・権限・コンテキストを分離した構造で実行することで品質と再現性が向上する。

## いつ使うのか

複数の専門的タスク（計画・実装・QA・デプロイ）を含む大規模ワークフロー、またはチームで再利用するオートメーション設計時

### 具体的な適用場面

- Claude Codeを業務・開発に本格導入する際に、Commands/Agents/Skills/Hooksの使い分けを体系的に学びたい場面
- チームでClaude Code運用ルールを標準化し、CLAUDE.mdやサブエージェント設計のベースラインを作りたい場面
- 自分のワークフローを見直してコンテキスト管理・並列開発・プランモードを効果的に活用したい場面

## やり方

1. `.claude/commands/<name>.md` にワークフロー起動用のスラッシュコマンドを定義（既存コンテキストにナレッジ注入）
2. `.claude/agents/<name>.md` に独立したコンテキスト・ツール・権限を持つサブエージェントを定義
3. `.claude/skills/<name>/SKILL.md` に再利用可能なスキルを定義（プログレッシブディスクロージャー対応）
4. コマンドがエントリーポイントとなりエージェントを呼び出し、エージェントがスキルを利用する階層を設計
5. `claude` → `/weather-orchestrator` のように呼び出して動作確認

### 入力

- タスク要件の定義
- 各エージェントのペルソナ・ツール・権限の設計
- .claude/ディレクトリ構造

### 出力

- 再利用可能なワークフローコマンド
- 自律実行可能なサブエージェント群
- 段階的に適用できるスキルセット

## 使うツール・ライブラリ

- Claude Code CLI
- .claude/commands/
- .claude/agents/
- .claude/skills/

## コード例

```
# .claude/commands/my-workflow.md
Run the following steps:
1. Use the @planner agent to create a spec
2. Use the @implementer agent to build it
3. Use the @reviewer skill to validate
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
