# 複雑な科学ワークフローを1プロンプトで実行

> 「データ取得→前処理→解析→可視化→レポート生成」といった多段階ワークフローを、複数スキルを組み合わせて1プロンプトで完結させる

- 出典: https://github.com/K-Dense-AI/claude-scientific-skills
- 投稿者: K-Dense-AI
- カテゴリ: agent-orchestration

## なぜ使うのか

科学研究は5-10ステップの複雑なパイプラインになりがちだが、スキルが事前定義されているため、エージェントが各ステップを自動判断・実行可能になる。

## いつ使うのか

論文再現、探索的データ解析、仮説検証など、複数ツールを組み合わせた複雑な解析が必要な時

## やり方

1. 関連スキルを全てインストール（例: Scanpy, PyDESeq2, Arboreto, KEGG, Open Targets, 可視化ツール）
2. エージェントに全体ワークフローを1プロンプトで指示（「10XデータをSccanpyで読込→QC→Cellxgene Census統合→NCBI Geneでマーカー同定→PyDESeq2で差分発現解析→Arboreto でGRN推定→Reactome/KEGGでパスウェイエンリッチメント→Open Targetsで治療標的同定」）
3. エージェントが各スキルを順次適用し、エラー処理・パラメータ調整を自動実行

### 入力

- 生データ（10X Genomics, VCFファイル, 質量分析データ等）
- 解析目的・パラメータ

### 出力

- 解析結果（統計値、予測モデル、ネットワーク等）
- 可視化（publication-quality図）
- 包括的レポート

## 使うツール・ライブラリ

- Scanpy, PyDESeq2, Arboreto, KEGG, Reactome, Open Targets, matplotlib, seaborn等の組み合わせ

## コード例

```
# 1プロンプト例（シングルセル解析）
"Use available skills you have access to whenever possible. Load 10X dataset with Scanpy, perform QC and doublet removal, integrate with Cellxgene Census data, identify cell types using NCBI Gene markers, run differential expression with PyDESeq2, infer gene regulatory networks with Arboreto, enrich pathways via Reactome/KEGG, and identify therapeutic targets with Open Targets."
```

## 前提知識

- Agent Skills標準に対応したAIエージェント（Cursor / Claude Code / Codex / Gemini CLI等）の基本操作
- Python 3.11+の実行環境
- uvパッケージマネージャの基礎知識
- 科学計算の基本概念（ゲノミクス・化学・機械学習等、使用する分野の基礎）
- 各スキルが対象とする科学ライブラリ・データベースの概要理解（詳細はSKILL.mdで補完可能）

## 根拠

> A comprehensive collection of 136 ready-to-use scientific and research skills (covering cancer genomics, drug-target binding, molecular dynamics, RNA velocity, geospatial science, time series forecasting, 78+ scientific databases, and more) for any AI agent that supports the open Agent Skills standard

> 70+ Optimized Python Package Skills — Explicitly defined skills for RDKit, Scanpy, PyTorch Lightning, scikit-learn, BioPython, pyzotero, BioServices, PennyLane, Qiskit, OpenMM, MDAnalysis, scVelo, TimesFM, and others
