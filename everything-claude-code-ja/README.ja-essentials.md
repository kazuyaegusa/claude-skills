# Everything Claude Code: まず知るべきポイント（日本語まとめ）

このドキュメントは、`everything-claude-code` を初めて触る人向けに、
「ここだけは理解しておくと迷わない」という要点を日本語で整理したものです。

---

## 1. このリポジトリは何か

これは**アプリ本体**ではなく、Claude Code / OpenCode を強化するための
**設定・運用テンプレート集**です。

主な中身:
- `agents/`: 専門サブエージェント定義（例: planner, code-reviewer）
- `commands/`: `/plan` のようなスラッシュコマンド定義
- `skills/`: 分野別の手順書・ベストプラクティス
- `rules/`: 常時守る開発ルール
- `hooks/`: イベント時に自動実行する処理
- `scripts/`: hooks を動かす Node.js 実装
- `tests/`: 設定・スクリプトが壊れていないかを確認するテスト

---

## 2. 最初に読む順番（おすすめ）

1. `README.md`
2. `rules/README.md`
3. `examples/CLAUDE.md`
4. `hooks/hooks.json`
5. `commands/plan.md`
6. `agents/planner.md`
7. `skills/tdd-workflow/SKILL.md`

この順番で読むと、
「全体像 → ルール → 実運用の自動化 → 実際のコマンド利用」
の流れで理解できます。

---

## 3. 重要コンセプト（ここが核）

### 3-1. Agents（役割分担）
- 例: `planner` は実装計画、`code-reviewer` はレビューに特化。
- 何でも1体でやらず、役割ごとに分けるのが前提。

### 3-2. Commands（すぐ実行できる定型プロンプト）
- `/plan`, `/tdd`, `/verify` など。
- 「毎回長文で指示する」手間を減らすための仕組み。

### 3-3. Skills（実装手順の知識ベース）
- コーディング規約、TDD、セキュリティ、言語別パターンなど。
- Rules が「何を守るか」、Skills が「どう実行するか」。

### 3-4. Hooks（自動ガードレール）
- 例: dev サーバー実行前の注意、編集後の整形、`console.log` 監査。
- ミスを「人の注意力」ではなく「自動化」で減らす思想。

### 3-5. Rules（常時ルール）
- `common/` + 言語別（`typescript/`, `python/`, `golang/`）の2層。
- 例: イミュータブル志向、テスト重視、セキュリティ必須チェック。

---

## 4. 導入時に必ず知っておくこと

### 4-1. Plugin導入だけでは Rules は入らない
`README.md` にある通り、Rules は手動コピーが必要です。

### 4-2. `hooks/hooks.json` は自動ロード前提
`.claude-plugin/PLUGIN_SCHEMA_NOTES.md` に重要注意があります。
`plugin.json` に hooks を明示すると、CLIバージョンによっては
重複読み込みエラーの原因になります。

### 4-3. MCPを増やしすぎると重くなる
READMEの推奨:
- 設定は多くてもOK
- 有効化は必要最小限（目安: 同時有効は10未満）

---

## 5. 実運用でよく使うコマンド

- `/plan`: 実装前に計画を作る
- `/tdd`: テスト先行で実装する
- `/code-review`: 品質/保守性のレビュー
- `/verify`: build/type/lint/test を検証
- `/build-fix`: ビルドエラー修正
- `/sessions`: セッション履歴の管理
- `/setup-pm`: パッケージマネージャ設定

迷ったら、`/plan` → `/tdd` → `/verify` の流れを基本にすると安定します。

---

## 6. セッション継続（地味に重要）

このリポジトリの hooks + scripts は、セッション継続を重視しています。

保存先:
- `~/.claude/sessions/`（作業メモ）
- `~/.claude/session-aliases.json`（別名管理）
- `~/.claude/skills/learned/`（学習スキル）

関連実装:
- `scripts/hooks/session-start.js`
- `scripts/hooks/session-end.js`
- `scripts/lib/session-manager.js`
- `scripts/lib/session-aliases.js`
- `commands/sessions.md`

---

## 7. 変更を加えるときの安全手順

1. 変更対象を決める
- コマンド修正: `commands/`
- エージェント修正: `agents/`
- スキル修正: `skills/`
- フック修正: `hooks/hooks.json` と `scripts/hooks/`

2. ローカルチェックを実行する
- `node tests/run-all.js`
- `node scripts/ci/validate-agents.js`
- `node scripts/ci/validate-commands.js`
- `node scripts/ci/validate-hooks.js`
- `node scripts/ci/validate-skills.js`
- `node scripts/ci/validate-rules.js`

3. 仕上げチェック
- `npx eslint scripts/**/*.js tests/**/*.js`
- `npx markdownlint "agents/**/*.md" "skills/**/*.md" "commands/**/*.md" "rules/**/*.md"`

---

## 8. よくあるハマりどころ

- `agents: Invalid input` のような曖昧エラー
  - 原因: plugin manifest の形式不一致
  - 対策: `.claude-plugin/PLUGIN_SCHEMA_NOTES.md` を先に読む

- hooks の重複エラー
  - 原因: auto-load される hooks を manifest に重複定義
  - 対策: README/NOTES の現行ルールに合わせる

- 環境差（npm/pnpm/yarn/bun）
  - 対策: `scripts/setup-package-manager.js` と `/setup-pm` を使う

- 長いセッションで文脈が崩れる
  - 対策: sessions 管理 + compact 戦略 + 必要なMCPだけ有効化

---

## 9. 初学者向けの最短スタート

1. `README.md` の Quick Start を実施
2. Rules を `common` + 自分の言語だけ導入
3. `/plan` と `/tdd` だけ先に使う
4. hooks は最初から全部盛りにせず、必要なものだけ有効化
5. まず1週間は「小さく試して改善」を繰り返す

---

## 10. このリポジトリの価値を一言で

「AIにお願いする」から、
「AI開発フローを設計して再現可能にする」へ進めるための土台です。

個人の好みを強く反映した設定なので、最初はそのまま使い、
次に自分のチーム/プロジェクト用に削っていくのが最も安全です。
