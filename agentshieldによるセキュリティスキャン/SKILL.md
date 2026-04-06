# AgentShieldによるセキュリティスキャン

> CLAUDE.md、settings.json、hooks、MCP設定を静的解析し、シークレット漏洩・権限過剰・インジェクションリスクを検出

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIエージェント環境は設定ファイルに機密情報や危険なコマンドを含みやすい。AgentShieldは1282テスト・102ルールでClaude Code Hackathon優勝の実績あり

## いつ使うのか

本番環境デプロイ前、新しいMCP server追加時、定期的なセキュリティ監査

## やり方

1. npx ecc-agentshield scan で現在のプロジェクトをスキャン
2. 14パターンのシークレット検出（API key, AWS key, GitHub PAT等）
3. 権限監査（MCP server許可範囲、hook実行権限）
4. hookインジェクション解析（悪意あるコマンド埋め込み）
5. MCP serverリスクプロファイリング
6. --opus フラグで3つのClaude Opus 4.6エージェント（攻撃者・防御者・監査者）による敵対的推論を実行
7. --fix で安全な問題を自動修正
8. JSON/Markdown/HTML形式で出力可能、CI/CDに組み込める（exit code 2でビルド停止）

### 入力

- CLAUDE.md
- settings.json
- hooks.json
- mcp-configs/*.json

### 出力

- A-Fグレードのリスク評価
- 検出された脆弱性リスト
- 修正推奨事項

## 使うツール・ライブラリ

- ecc-agentshield（npm）
- Claude Opus 4.6（--opusモード）

## コード例

```
# 基本スキャン
npx ecc-agentshield scan

# 自動修正
npx ecc-agentshield scan --fix

# 深層解析（3エージェント敵対的推論）
npx ecc-agentshield scan --opus --stream

# セキュアな設定を新規生成
npx ecc-agentshield init
```

## 前提知識

- Claude Code CLI v2.1.0以降、またはCursor/OpenCode/Codexのいずれか
- npm/pnpm/yarn/bunのいずれかのパッケージマネージャー
- Gitの基本操作（クローン、コミット）
- JSON/YAML形式の理解
- 対象言語のテストフレームワーク（pytest/jest/go test等）の基礎知識
- （オプション）claude -p サブスクリプション認証（継続学習に必要）

## 根拠

> 「Not just configs. A complete system: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development.」

> 「Production-ready agents, skills, hooks, rules, MCP configurations, and legacy command shims evolved over 10+ months of intensive daily use building real products.」

> 「Won the Anthropic x Forum Ventures hackathon in Sep 2025 with @DRodriguezFX — built zenith.chat entirely using Claude Code.」

> 「AgentShield integration — /security-scan skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules」

> 「Cursor has more hook events than Claude Code (20 vs 8). The .cursor/hooks/adapter.js module transforms Cursor's stdin JSON to Claude Code's format」
