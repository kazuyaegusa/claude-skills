# 100+データベースを統一database-lookupスキルで検索

> PubChem, ChEMBL, UniProt, COSMIC, ClinicalTrials.gov等78データベースへのREST API呼び出しを1つのスキルに集約し、エージェントが横断検索可能にする

- 出典: https://github.com/K-Dense-AI/claude-scientific-skills
- 投稿者: K-Dense-AI
- カテゴリ: agent-orchestration

## なぜ使うのか

科学研究は複数DBの統合が必須だが、各API仕様を毎回調べるのは非効率。統一スキルで「遺伝子→タンパク質→薬剤→臨床試験」の流れを1プロンプトで実行できる。

## いつ使うのか

複数の科学データベースを横断して情報収集する必要がある時（創薬、バリアント解釈、文献調査等）

## やり方

1. database-lookupスキルをインストール
2. エージェントに「ChEMBLでEGFR阻害剤を検索→UniProtでタンパク質情報取得→ClinicalTrials.govで関連試験検索」と指示
3. スキルが各DBのREST APIを自動呼び出し、結果を統合

### 入力

- 検索キーワード（遺伝子名、化合物名、疾患名等）
- 対象データベース名（PubChem, ChEMBL, UniProt等）

### 出力

- 各データベースからの検索結果（JSON/構造化データ）
- 統合された知見

## 使うツール・ライブラリ

- database-lookup skill
- 78+ REST API (PubChem, ChEMBL, UniProt, COSMIC, ClinicalTrials.gov, FDA, KEGG, Reactome, STRING, ClinVar等)

## コード例

```
# プロンプト例
"ChEMBLでEGFR阻害剤(IC50 < 50nM)を検索→UniProtでタンパク質情報→ClinicalTrials.govで関連試験検索→統合レポート作成"
```

## 前提知識

- Agent Skills標準に対応したAIエージェント（Cursor / Claude Code / Codex / Gemini CLI等）の基本操作
- Python 3.11+の実行環境
- uvパッケージマネージャの基礎知識
- 科学計算の基本概念（ゲノミクス・化学・機械学習等、使用する分野の基礎）
- 各スキルが対象とする科学ライブラリ・データベースの概要理解（詳細はSKILL.mdで補完可能）

## 根拠

> 100+ Scientific & Financial Databases — A unified database-lookup skill provides direct access to 78 public databases (PubChem, ChEMBL, UniProt, COSMIC, ClinicalTrials.gov, FRED, USPTO, and more)
