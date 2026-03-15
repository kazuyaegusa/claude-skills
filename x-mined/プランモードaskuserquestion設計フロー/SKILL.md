# プランモード+AskUserQuestion設計フロー

> 作業開始時は必ずプランモードで開始し、要件が曖昧な場合はClaudeにAskUserQuestionツールを使ったインタビューをさせてから実装セッションを別途開始する。

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

最初に詳細な仕様を固めることで実装の手戻りが激減する。Claude作成者のBoris Chernyも「always start with plan mode」を最重要プラクティスとして挙げている。

## いつ使うのか

新機能の実装開始時、要件が複数フェーズにまたがる複雑なタスク、チームへの作業委譲前

### 具体的な適用場面

- Claude Codeを業務・開発に本格導入する際に、Commands/Agents/Skills/Hooksの使い分けを体系的に学びたい場面
- チームでClaude Code運用ルールを標準化し、CLAUDE.mdやサブエージェント設計のベースラインを作りたい場面
- 自分のワークフローを見直してコンテキスト管理・並列開発・プランモードを効果的に活用したい場面

## やり方

1. `claude`起動後すぐにプランモードに切り替え（または`/plan`コマンドで起動）
2. 要件が不明確な場合：「AskUserQuestionツールを使って要件をインタビューしてください」と指示
3. Claudeからの質問に回答して仕様を確定
4. 確定した仕様でフェーズ別計画を作成（各フェーズにunit/automation/integrationテストを含める）
5. 計画をレビューするためにセカンドClaudeインスタンスかクロスモデル（Codex等）でレビューを依頼
6. 計画承認後、新しいセッションで実装開始

### 入力

- 大まかな要件・アイデア
- プロジェクトコンテキスト（CLAUDE.md）

### 出力

- フェーズ別実装計画
- テスト基準を含む詳細仕様
- 各フェーズのゲート条件

## 使うツール・ライブラリ

- Claude Code plan mode
- AskUserQuestionツール
- /plan コマンド

## コード例

```
None
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
