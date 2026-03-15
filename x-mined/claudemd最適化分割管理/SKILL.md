# CLAUDE.md最適化・分割管理

> CLAUDE.mdを200行以下に保ち、大きくなった場合は`.claude/rules/`ディレクトリに分割して管理する。モノレポでは階層別に複数のCLAUDE.mdを配置する。

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

CLAUDE.mdが長すぎるとClaudeが指示を無視する確率が上がる（実例あり）。分割することで関連する指示が確実にロードされ、メンテナンス性も向上する。

## いつ使うのか

CLAUDE.mdが200行を超えてきた時、またはClaudeが明示的な指示を無視し始めた時

### 具体的な適用場面

- Claude Codeを業務・開発に本格導入する際に、Commands/Agents/Skills/Hooksの使い分けを体系的に学びたい場面
- チームでClaude Code運用ルールを標準化し、CLAUDE.mdやサブエージェント設計のベースラインを作りたい場面
- 自分のワークフローを見直してコンテキスト管理・並列開発・プランモードを効果的に活用したい場面

## やり方

1. 現在のCLAUDE.mdの行数を確認（目標200行以下）
2. テーマ別に`.claude/rules/coding-style.md`、`.claude/rules/testing.md`等に分割
3. CLAUDE.mdから`@.claude/rules/coding-style.md`のように`@path`でインポート
4. モノレポの場合はルートCLAUDE.mdと各パッケージ配下のCLAUDE.mdに分離
5. 定期的に陳腐化した指示を削除・更新

### 入力

- 既存のCLAUDE.md
- プロジェクト構造・ルール体系

### 出力

- 200行以下のCLAUDE.md
- .claude/rules/配下の分割ルールファイル

## 使うツール・ライブラリ

- CLAUDE.md
- .claude/rules/ディレクトリ
- @pathインポート構文

## コード例

```
# CLAUDE.md（200行以下に保つ）
@.claude/rules/coding-style.md
@.claude/rules/testing.md
@.claude/rules/git-workflow.md
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
