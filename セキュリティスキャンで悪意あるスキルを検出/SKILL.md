# セキュリティスキャンで悪意あるスキルを検出

> Cisco AI Defense Skill Scannerを使い、スキルがプロンプトインジェクション・データ流出・悪意あるコードを含まないか検証する

- 出典: https://github.com/K-Dense-AI/claude-scientific-skills
- 投稿者: K-Dense-AI
- カテゴリ: claude-code-workflow

## なぜ使うのか

スキルは任意コード実行・ネットワークリクエスト・ファイル変更が可能なため、悪意あるスキルはシステムを危険に晒す。インストール前のスキャンでリスク低減。

## いつ使うのか

コミュニティ提供のスキルや未検証のスキルをインストールする前

## やり方

1. Cisco AI Defense Skill Scannerをインストール（uv pip install cisco-ai-skill-scanner）
2. スキルディレクトリをスキャン（skill-scanner scan /path/to/skill --use-behavioral）
3. レポートを確認し、疑わしいパターンがあれば精査
4. 安全と判断したスキルのみインストール

### 入力

- スキルディレクトリ（SKILL.mdファイル含む）

### 出力

- セキュリティスキャンレポート
- 検出された脅威パターン

## 使うツール・ライブラリ

- cisco-ai-skill-scanner (https://github.com/cisco-ai-defense/skill-scanner)

## コード例

```
# スキャナインストール
uv pip install cisco-ai-skill-scanner

# スキルスキャン
skill-scanner scan /path/to/skill --use-behavioral
```

## 前提知識

- Agent Skills標準に対応したAIエージェント（Cursor / Claude Code / Codex / Gemini CLI等）の基本操作
- Python 3.11+の実行環境
- uvパッケージマネージャの基礎知識
- 科学計算の基本概念（ゲノミクス・化学・機械学習等、使用する分野の基礎）
- 各スキルが対象とする科学ライブラリ・データベースの概要理解（詳細はSKILL.mdで補完可能）

## 根拠

> A comprehensive collection of 136 ready-to-use scientific and research skills (covering cancer genomics, drug-target binding, molecular dynamics, RNA velocity, geospatial science, time series forecasting, 78+ scientific databases, and more) for any AI agent that supports the open Agent Skills standard

> These skills enable your AI agent to seamlessly work with specialized scientific libraries, databases, and tools across multiple scientific domains. While the agent can use any Python package or API on its own, these explicitly defined skills provide curated documentation and examples that make it significantly stronger and more reliable

> 100+ Scientific & Financial Databases — A unified database-lookup skill provides direct access to 78 public databases (PubChem, ChEMBL, UniProt, COSMIC, ClinicalTrials.gov, FRED, USPTO, and more)

> 70+ Optimized Python Package Skills — Explicitly defined skills for RDKit, Scanpy, PyTorch Lightning, scikit-learn, BioPython, pyzotero, BioServices, PennyLane, Qiskit, OpenMM, MDAnalysis, scVelo, TimesFM, and others

> Simply copy the skill folders into your skills directory and your AI agent will automatically discover and use them.
