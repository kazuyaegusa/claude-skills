# プラグインベース統合インストール

> Everything Claude Code（ECC）をClaude Codeプラグインとして一括インストールし、39エージェント・178スキル・72コマンドを即座に利用可能にする

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動で個別ファイルをコピーする手間を排除し、アップデート追従を容易にするため。npmパッケージ化により依存関係管理も自動化される

## いつ使うのか

初回セットアップ時、または最新版への更新時

## やり方

1. `/plugin marketplace add https://github.com/affaan-m/everything-claude-code` でマーケットプレース登録
2. `/plugin install ecc@ecc` でプラグインインストール
3. rules/ ディレクトリは手動コピー（`cp -r rules/common ~/.claude/rules/` 等、必要な言語のみ選択）
4. hooks.json の内容を ~/.claude/settings.json にマージ
5. MCP設定を ~/.claude/settings.json または .mcp.json に追加

### 入力

- Claude Code CLI v2.1.0以降
- npm/pnpm/yarn/bunいずれかのパッケージマネージャー

### 出力

- ~/.claude/agents/ に39エージェント
- ~/.claude/skills/ に178スキル
- ~/.claude/commands/ に72コマンド
- ~/.claude/rules/ に言語別ルール
- hooks.json の自動ロード

## 使うツール・ライブラリ

- Claude Code CLI
- npm/pnpm/yarn/bun
- ecc-universal（npmパッケージ）

## コード例

```
# プラグインインストール
/plugin marketplace add https://github.com/affaan-m/everything-claude-code
/plugin install ecc@ecc

# ルール手動コピー（TypeScript例）
cp -r everything-claude-code/rules/common ~/.claude/rules/
cp -r everything-claude-code/rules/typescript ~/.claude/rules/
```

## 前提知識

- Claude Code CLI v2.1.0以降、またはCursor/OpenCode/Codexのいずれか
- npm/pnpm/yarn/bunのいずれかのパッケージマネージャー
- Gitの基本操作（クローン、コミット）
- JSON/YAML形式の理解
- 対象言語のテストフレームワーク（pytest/jest/go test等）の基礎知識
- （オプション）claude -p サブスクリプション認証（継続学習に必要）

## 根拠

> 「Won the Anthropic x Forum Ventures hackathon in Sep 2025 with @DRodriguezFX — built zenith.chat entirely using Claude Code.」

> 「CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: 50 — Compacts earlier — better quality in long sessions」

> 「AgentShield integration — /security-scan skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules」

> 「Cursor has more hook events than Claude Code (20 vs 8). The .cursor/hooks/adapter.js module transforms Cursor's stdin JSON to Claude Code's format」

> 「Codex macOS app + CLI support — Direct AGENTS.md-based Codex support, installer targeting, and Codex docs」
