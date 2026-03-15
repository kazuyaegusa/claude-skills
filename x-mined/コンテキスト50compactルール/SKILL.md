# コンテキスト50%compactルール

> コンテキスト使用率が50%に達したタイミングで手動で`/compact`を実行し、新しいタスクに切り替える際は`/clear`でコンテキストをリセットする。

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

コンテキストが満杯に近づくと「agent dumb zone」と呼ばれる状態になり、Claudeの応答品質が劣化する。早めのcompactで品質を維持できる。

## いつ使うのか

長時間セッション中にコンテキスト使用率が50%に達した時、または別の独立したタスクに切り替える時

### 具体的な適用場面

- Claude Codeを業務・開発に本格導入する際に、Commands/Agents/Skills/Hooksの使い分けを体系的に学びたい場面
- チームでClaude Code運用ルールを標準化し、CLAUDE.mdやサブエージェント設計のベースラインを作りたい場面
- 自分のワークフローを見直してコンテキスト管理・並列開発・プランモードを効果的に活用したい場面

## やり方

1. `/context`コマンドでコンテキスト使用率を定期確認
2. 使用率が50%前後になったら`/compact`を実行して要約
3. 別タスクに切り替える際は`/compact`ではなく`/clear`でリセット
4. ステータスラインを設定してコンテキスト使用率を常時表示（`.claude/settings.json`で設定）
5. compaction中にエラーが出た場合は`/model`で1Mトークンモデルに切り替えてから再実行

### 入力

- 進行中のセッション
- コンテキスト使用率の監視

### 出力

- 要約された軽量コンテキスト
- 継続的に高品質な応答

## 使うツール・ライブラリ

- /compact
- /clear
- /context
- /model
- status line設定

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
