# ecc-agentshieldで多言語セキュリティスキャン実行

> 102ルール・1,282テストを持つecc-agentshieldを使い、Shell/TypeScript/Python/Go/Java/Perl/Markdownの7言語を横断してコードの脆弱性を自動検出する

- 出典: https://x.com/l_go_mrk/status/2037489559186145787
- 投稿者: AI駆動塾
- カテゴリ: claude-code-workflow

## なぜ使うのか

セキュリティルールを自前で整備すると数ヶ月かかるが、ECCのルールセットを使えば即日102ルールの自動チェック体制が整う。多言語混在プロジェクトでの抜け漏れを防げる

## いつ使うのか

PRマージ前、依存パッケージ更新後、または本番リリース前のゲートチェックとして実行するとき

### 具体的な適用場面

- 新規プロジェクト開始時にClaude Codeのデフォルト能力をゼロから拡張したい場合
- PRマージ前・本番リリース前に多言語コードベースを横断してセキュリティ脆弱性を自動検出したい場合
- コード生成・テスト・セキュリティレビューを同一セッション内で並列処理したい場合

## やり方

1. `npx ecc-agentshield` でセキュリティスキャンツール単体をインストール
2. プロジェクトルートでClaude Code内から `/security-scan` スラッシュコマンドを実行
3. コードレビューと組み合わせる場合は `/security-review` を使用
4. 検出結果はルール番号・言語・重大度・修正提案付きで出力される

### 入力

- スキャン対象のコードベース（Shell/TS/Python/Go/Java/Perl/Markdownのいずれか）
- npx実行可能なNode.js環境

### 出力

- 違反ルール一覧（ルール番号・ファイルパス・行番号付き）
- 重大度別の修正優先度リスト（102ルール適用結果）

## 使うツール・ライブラリ

- ecc-agentshield (npm package)
- npx

## コード例

```
# ツールインストール
npx ecc-agentshield

# Claude Code内から実行
/security-scan
# または
/security-review
```

## 前提知識

- Claude Code CLIがインストールされていること（`claude --version` で確認）
- Node.js / npxが使用可能な環境（ecc-universal/ecc-agentshieldのインストールに必要）
- GitHubアカウント（GitHub App経由のインストールを使う場合）

## 根拠

> 28の専門サブエージェントが連携して動く

> 125以上のSkillsをプリビルドで搭載

> 60以上のスラッシュコマンド

> セキュリティスキャン内蔵（102ルール、1,282テスト）

> 7言語対応
