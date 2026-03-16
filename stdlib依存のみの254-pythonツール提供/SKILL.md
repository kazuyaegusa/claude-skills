# stdlib依存のみの254 Pythonツール提供

> pip install不要、Python標準ライブラリのみで動作する254個のCLIツールを各スキルに同梱

- 出典: https://github.com/alirezarezvani/claude-skills
- 投稿者: alirezarezvani
- カテゴリ: claude-code-workflow

## なぜ使うのか

依存関係の管理コスト削減、環境再現性の向上、セキュリティリスクの低減（外部パッケージの脆弱性を回避）

## いつ使うのか

環境構築を最小化したい、Dockerコンテナサイズを抑えたい、外部依存を避けたい場合

## やり方

1. 必要な機能を標準ライブラリのみで実装（json, argparse, pathlib, re等を活用）
2. scripts/ ディレクトリ配下に配置
3. --help オプションで使い方を提供
4. JSON出力オプションでパイプライン統合を容易化

### 入力

- タスク固有の入力データ（CSV, JSON, テキストファイル等）
- コマンドライン引数

### 出力

- 標準出力またはJSONフォーマットの結果
- 生成されたファイル（レポート、設定ファイル等）

## 使うツール・ライブラリ

- Python標準ライブラリ（json, argparse, pathlib, csv, re, subprocess等）

## コード例

```
# SaaS メトリクス計算
python3 finance/saas-metrics-coach/scripts/metrics_calculator.py \
  --mrr 80000 --customers 200 --churned 3 --json

# セキュリティ監査
python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py \
  /path/to/skill/

# RICE優先順位付け
python3 product-team/product-manager-toolkit/scripts/rice_prioritizer.py \
  features.csv
```

## 前提知識

- Claude CodeまたはOpenAI Codex等のAIコーディングツールの基本的な使い方
- SKILL.md形式やエージェント概念の理解（ただしREADMEに説明あり）
- Bash/シェルスクリプトの基本知識（インストールスクリプト実行用）
- Python 3.x の実行環境（CLIツール使用時）
- Git/GitHub の基本操作

## 根拠

> 「254 CLI scripts (all stdlib-only, zero pip installs)」

> 「./scripts/convert.sh --tool all → Convert all skills to all tools (takes ~15 seconds)」
