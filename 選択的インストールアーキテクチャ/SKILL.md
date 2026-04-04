# 選択的インストールアーキテクチャ

> マニフェスト駆動のインストールパイプライン（install-plan.js + install-apply.js）により、必要なコンポーネントのみをターゲット別に選択インストールし、状態ストアで追跡・増分更新を可能にする

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

全言語・全スキル・全エージェントを一括インストールするとディスク容量・メンテナンスコストが増大。プロジェクトに必要なコンポーネントのみをインストールし、後から追加・更新できる柔軟性が必要

## いつ使うのか

特定言語スタックのみ使用するプロジェクト、ディスク容量が限られている環境、段階的にECCを導入したい場合

## やり方

1. ./install.sh --target <harness> <languages> で対象ハーネス（claude/cursor/codex/opencode/antigravity）と言語を指定 2. install-plan.js がマニフェストを読み、必要なルール・スキル・エージェント・フックを計算 3. install-apply.js が実際のファイルコピー・マージを実行 4. 状態ストア（.ecc-state.json等）がインストール済みコンポーネントを記録 5. 再実行時は差分のみを適用（増分更新）

### 入力

- --target フラグ（claude/cursor/codex/opencode/antigravity）
- --profile フラグ（minimal/standard/full）
- 言語リスト（typescript/python/golang/swift/php/java/kotlin/rust/cpp/perl）

### 出力

- 選択した言語の rules/ のみインストール
- 選択したハーネス用の設定ファイル（hooks.json/.cursor/hooks/等）
- .ecc-state.json（インストール状態記録）
- 増分更新による高速再インストール

## 使うツール・ライブラリ

- install.sh（macOS/Linux）/ install.ps1（Windows）
- install-plan.js, install-apply.js
- 状態ストア（SQLite/JSON）

## コード例

```
# TypeScriptのみインストール（Claude Code用）
./install.sh typescript

# Python + Go（Cursor用）
./install.sh --target cursor python golang

# フルプロファイル（全言語・全スキル）
./install.sh --profile full

# Antigravity用にTypeScript
./install.sh --target antigravity typescript

# 増分更新（差分のみ適用）
./install.sh --update typescript
```

## 前提知識

- Claude Code CLI v2.1.0以上の基本操作知識
- 使用する言語スタック（TypeScript/Python/Go等）の基礎知識
- git、npm/pnpm/yarn/bunの基本操作
- JSON/YAML/TOML形式の理解
- CI/CDパイプラインの基礎（AgentShield統合時）
- セキュリティベストプラクティスの基本（OWASP Top 10等）

## 根拠

> 「Selective install architecture — Manifest-driven install pipeline with install-plan.js and install-apply.js for targeted component installation」
