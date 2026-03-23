# 検証ループ（Eval Harness）

> ビルド・テスト・リント・型チェック・セキュリティスキャンを自動実行し、結果を評価。pass@k メトリクスで品質を定量化

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

AI が書いたコードをそのまま信用するのは危険。自動検証ループで機械的に品質を担保する

## いつ使うのか

本番デプロイ前、PR 作成前、大規模リファクタリング後

## やり方

1. /verify コマンドで検証ループを起動
2. skills/verification-loop/SKILL.md に定義された順序で実行（build → test → lint → typecheck → security）
3. 各ステップの結果を .claude/checkpoints/ に保存
4. 失敗時は自動的に修正を試み、再検証
5. pass@k（k 回試行して何回成功したか）を記録

### 入力

- 検証スクリプト（package.json の scripts）
- /verify, /checkpoint コマンド

### 出力

- .claude/checkpoints/*.json（検証結果）
- pass@k メトリクス
- 自動修正の試行回数

## 使うツール・ライブラリ

- Claude Code verification-loop skill
- npm/pnpm/yarn/bun scripts
- Jest/Vitest, ESLint, TypeScript, AgentShield

## コード例

```
# verification-loop の実行順序
1. npm run build
2. npm run test -- --coverage
3. npm run lint
4. npm run typecheck
5. npx ecc-agentshield scan
```

## 前提知識

- Claude Code CLI v2.1.0 以降のインストール
- Node.js 18 以降（hooks/scripts の実行に必要）
- Git の基本操作（clone, commit, PR）
- npm/pnpm/yarn/bun のいずれか
- JSON/YAML/TOML の基本文法
- 使用する言語のツールチェーン（TypeScript なら tsc, Python なら pytest など）

## 根拠

> 「These configs are battle-tested across multiple production applications.」

> 「AgentShield integration — /security-scan skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules」
