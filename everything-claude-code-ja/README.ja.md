# Everything Claude Code 完全ガイド（日本語）

このファイルは、英語READMEを読めない方向けに、  
このリポジトリで**理解すべき内容を日本語でまとめた実用ガイド**です。

対象ディレクトリ: `everything-claude-code`（このプロジェクト直下）

---

## 0. 最初に結論

このリポジトリは、普通のWebアプリ本体ではありません。  
Claude Code / OpenCode を強化するための「設定・ワークフロー集」です。

特に重要なのは次の5つです。

1. `commands/`（スラッシュコマンド）
2. `agents/`（専門サブエージェント）
3. `skills/`（作業手順の知識）
4. `rules/`（常時守るルール）
5. `hooks/hooks.json`（自動化フック）

---

## 1. このリポジトリの正体

### 1-1. 何が入っているか

- `agents/`  
  役割別のAI担当者定義（設計担当、レビュー担当など）
- `commands/`  
  `/plan` などの短縮コマンド
- `skills/`  
  TDD、セキュリティ、言語別ベストプラクティス
- `rules/`  
  いつでも守る規約
- `hooks/`  
  ツール実行前後・セッション開始終了の自動処理
- `scripts/`  
  hooks を実際に動かす Node.js スクリプト
- `tests/`  
  設定やスクリプトの品質チェック
- `.claude-plugin/`  
  Claude Code 向けプラグイン定義
- `.opencode/`  
  OpenCode 向け設定・実装

### 1-2. 何が「入っていない」か

- 一般的な `src/` アプリ本体（このリポジトリの主目的ではない）
- 単一言語のライブラリ本体

---

## 2. まず覚える用語

### 2-1. Agent

特定タスク専門のサブエージェント。  
例: `planner`（計画作成）、`code-reviewer`（レビュー）。

### 2-2. Command

`/plan` のようなショートカット命令。  
長い指示文を毎回書かずに済む。

### 2-3. Skill

タスクの進め方を記述した知識モジュール。  
「どう進めるか」の実務手順。

### 2-4. Rule

常時守るルール。  
「何を守るか」を定義。

### 2-5. Hook

イベント時に自動実行される処理。  
例: 編集後フォーマット、`console.log` 警告。

---

## 3. 使い始める最短手順（Claude Code）

### 3-1. 前提

- Claude Code CLI は **v2.1.0以上** 推奨
- Node.js が利用可能な環境

### 3-2. プラグイン導入

```bash
/plugin marketplace add affaan-m/everything-claude-code
/plugin install everything-claude-code@everything-claude-code
```

### 3-3. 重要: Rulesは手動導入が必要

プラグインだけでは `rules/` は配布されません。  
必要なルールを手動でコピーします。

```bash
# 共通ルール（必須）
cp -r rules/common/* ~/.claude/rules/

# 言語別（必要なものだけ）
cp -r rules/typescript/* ~/.claude/rules/
cp -r rules/python/* ~/.claude/rules/
cp -r rules/golang/* ~/.claude/rules/
```

---

## 4. 最重要の注意点（ここは必読）

### 4-1. hooks重複定義に注意

`hooks/hooks.json` はCLI側の挙動で自動ロードされる前提があります。  
`.claude-plugin/plugin.json` 側に重複して hooks を定義すると、  
バージョンによっては重複エラーになります。

詳細は: `.claude-plugin/PLUGIN_SCHEMA_NOTES.md`

### 4-2. MCPは有効化しすぎない

MCPを大量に同時有効化すると、文脈効率やコストが悪化します。  
「設定は多く、同時有効は少なく」が基本です。

### 4-3. まず全部を採用しない

最初から全機能を使うと混乱します。  
まずは `plan/tdd/verify` と最小hooksで開始し、徐々に追加してください。

---

## 5. 推奨ワークフロー（初心者向け）

1. `/plan` で実装計画を作る  
2. `/tdd` でテスト先行で実装する  
3. `/verify` で build/type/lint/test を確認  
4. `/code-review` で品質を確認  
5. 必要なら `/build-fix` でエラー修正

この順番で進めると事故が減ります。

---

## 6. コマンド一覧（このリポジトリの31個）

`commands/` にある主要コマンドです。

- `/build-fix` - ビルド/型エラー修正
- `/checkpoint` - 検証状態の記録
- `/code-review` - コードレビュー
- `/e2e` - E2Eテスト生成・実行支援
- `/eval` - 評価実行
- `/evolve` - instincts 進化/クラスタ化
- `/go-build` - Goビルドエラー修正
- `/go-review` - Goコードレビュー
- `/go-test` - Go向けTDD
- `/instinct-export` - instincts エクスポート
- `/instinct-import` - instincts インポート
- `/instinct-status` - instincts 状態確認
- `/learn` - セッション学習抽出
- `/multi-backend` - 複数バックエンド連携計画
- `/multi-execute` - 複数エージェント実行
- `/multi-frontend` - 複数フロント連携計画
- `/multi-plan` - 複数タスク分解計画
- `/multi-workflow` - 汎用マルチワークフロー
- `/orchestrate` - オーケストレーション
- `/plan` - 実装計画作成
- `/pm2` - PM2運用補助
- `/python-review` - Pythonコードレビュー
- `/refactor-clean` - 不要コード整理
- `/sessions` - セッション管理
- `/setup-pm` - パッケージマネージャ設定
- `/skill-create` - スキル生成
- `/tdd` - テスト駆動開発
- `/test-coverage` - カバレッジ確認
- `/update-codemaps` - コードマップ更新
- `/update-docs` - ドキュメント更新
- `/verify` - 総合検証

---

## 7. エージェント一覧（13個）

`agents/` にある担当者です。

- `architect` - 設計判断
- `build-error-resolver` - ビルドエラー修正
- `code-reviewer` - 品質レビュー
- `database-reviewer` - DBレビュー
- `doc-updater` - 文書更新
- `e2e-runner` - E2E支援
- `go-build-resolver` - Goビルド修正
- `go-reviewer` - Goレビュー
- `planner` - 計画立案
- `python-reviewer` - Pythonレビュー
- `refactor-cleaner` - リファクタ/整理
- `security-reviewer` - セキュリティレビュー
- `tdd-guide` - TDD推進

---

## 8. Rulesの理解（超重要）

### 8-1. 構造

- `rules/common/`（共通・必須）
- `rules/typescript/`
- `rules/python/`
- `rules/golang/`

### 8-2. よく出る方針

- イミュータブル重視
- 例外・エラーハンドリング明示
- 入力検証必須
- テスト重視（80%以上目標）
- セキュリティチェック必須

---

## 9. Hooksの理解（自動化の中心）

`hooks/hooks.json` で、以下イベントに処理をぶら下げます。

- `PreToolUse`
- `PostToolUse`
- `PreCompact`
- `SessionStart`
- `SessionEnd`
- `Stop`

このリポジトリの代表的自動化:

- 長時間コマンドの tmux 利用促し
- JS/TS編集後の整形
- TypeScriptチェック補助
- `console.log` 警告
- セッション開始/終了時の状態管理

---

## 10. セッション継続と学習

### 10-1. セッション保存

関連スクリプト:

- `scripts/hooks/session-start.js`
- `scripts/hooks/session-end.js`
- `scripts/lib/session-manager.js`
- `scripts/lib/session-aliases.js`

主な保存先:

- `~/.claude/sessions/`
- `~/.claude/session-aliases.json`
- `~/.claude/skills/learned/`

### 10-2. continuous-learning

短いセッションはスキップし、十分なやり取りがあれば  
再利用可能なパターン抽出を促す設計です。

---

## 11. パッケージマネージャ検出の仕組み

`scripts/lib/package-manager.js` で優先順に判定します。

1. 環境変数 `CLAUDE_PACKAGE_MANAGER`
2. `.claude/package-manager.json`
3. `package.json` の `packageManager`
4. ロックファイル検出
5. `~/.claude/package-manager.json`
6. 利用可能なものへフォールバック

設定補助:
- `scripts/setup-package-manager.js`
- `/setup-pm`

---

## 12. テストとCI（壊していないか確認）

ローカル:

```bash
node tests/run-all.js
node scripts/ci/validate-agents.js
node scripts/ci/validate-commands.js
node scripts/ci/validate-hooks.js
node scripts/ci/validate-skills.js
node scripts/ci/validate-rules.js
```

CIワークフロー:

- `.github/workflows/ci.yml`（総合CI）
- `.github/workflows/reusable-test.yml`
- `.github/workflows/reusable-validate.yml`
- `.github/workflows/release.yml`
- `.github/workflows/maintenance.yml`

---

## 13. どこを編集すれば何が変わるか

- コマンド文言を変える: `commands/*.md`
- エージェントの役割を変える: `agents/*.md`
- スキルを追加する: `skills/<name>/SKILL.md`
- 自動処理を変える: `hooks/hooks.json` と `scripts/hooks/*.js`
- ルールを変える: `rules/common/*` + 言語別
- OpenCode側を変える: `.opencode/*`

---

## 14. 初学者向け: 1週間の導入計画

### Day 1
- `README.ja.md`（このファイル）を読み切る
- `rules/common` を導入

### Day 2
- `/plan` と `/tdd` を1タスクだけ使う

### Day 3
- `/verify` で検証フローを体験

### Day 4
- `hooks/hooks.json` の内容を1つだけ有効/調整

### Day 5
- `sessions` コマンドで継続運用を試す

### Day 6
- 言語別ルール（TS/Python/Go）を必要分だけ追加

### Day 7
- 自分用に不要機能を削る（最重要）

---

## 15. よくある詰まりポイント

1. エラーが曖昧で原因不明  
   - まず `.claude-plugin/PLUGIN_SCHEMA_NOTES.md` を確認

2. hooks が効かない / 重複エラー  
   - hooks 宣言重複を疑う

3. 何から始めるか分からない  
   - `/plan` → `/tdd` → `/verify` だけに絞る

4. 設定が多すぎて混乱  
   - 一度「最小構成」に戻し、必要なものだけ再追加

---

## 16. 最後に（重要）

このリポジトリは「そのまま全部使う」より、  
**自分の開発スタイルに合わせて削っていく**方がうまくいきます。

最初の目標は「完全理解」ではなく、次の3点です。

1. 計画して実装する（`/plan`）
2. テストで守る（`/tdd`）
3. 最後に検証する（`/verify`）

この3つが安定すると、他機能は後から安全に拡張できます。

