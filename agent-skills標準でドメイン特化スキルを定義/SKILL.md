# Agent Skills標準でドメイン特化スキルを定義

> 科学計算ライブラリ・データベース・ツールをAgent Skills仕様のSKILL.mdファイルとして構造化し、AIエージェントが自動検出・利用可能にする

- 出典: https://github.com/K-Dense-AI/claude-scientific-skills
- 投稿者: K-Dense-AI
- カテゴリ: claude-code-workflow

## なぜ使うのか

エージェントは任意のパッケージを使えるが、事前定義されたドキュメント・例・ベストプラクティスがあると精度・速度・信頼性が大幅向上。科学ワークフローは複雑なため明示的スキル定義が必須。

## いつ使うのか

科学計算・研究タスクをAIエージェントに任せる際、毎回APIドキュメントから説明するのではなく即座に実行させたい時

## やり方

1. 各科学ライブラリ/データベース用にディレクトリを作成
2. SKILL.mdファイルに、概要・ユースケース・コード例・ベストプラクティス・リファレンスを記載（Agent Skills仕様に準拠）
3. スキルディレクトリを~/.cursor/skills/等にコピー
4. エージェントが自動検出し、関連タスク時に該当スキルを適用

### 入力

- 科学ライブラリ/データベース/ツールの公式ドキュメント
- 実用的なコード例・ワークフロー例
- ベストプラクティス・注意点

### 出力

- Agent Skills標準準拠のSKILL.mdファイル
- エージェントが自動検出・利用可能なスキルディレクトリ

## 使うツール・ライブラリ

- Agent Skills標準 (https://agentskills.io/)
- Cursor / Claude Code / Codex / Gemini CLI

## コード例

```
# ディレクトリ構成例
scientific-skills/
  scanpy/
    SKILL.md  # フロントマター + ドキュメント + 例
  rdkit/
    SKILL.md
  ...

# グローバルインストール例
cp -r claude-scientific-skills/scientific-skills/* ~/.cursor/skills/
```

## 前提知識

- Agent Skills標準に対応したAIエージェント（Cursor / Claude Code / Codex / Gemini CLI等）の基本操作
- Python 3.11+の実行環境
- uvパッケージマネージャの基礎知識
- 科学計算の基本概念（ゲノミクス・化学・機械学習等、使用する分野の基礎）
- 各スキルが対象とする科学ライブラリ・データベースの概要理解（詳細はSKILL.mdで補完可能）

## 根拠

> A comprehensive collection of 136 ready-to-use scientific and research skills (covering cancer genomics, drug-target binding, molecular dynamics, RNA velocity, geospatial science, time series forecasting, 78+ scientific databases, and more) for any AI agent that supports the open Agent Skills standard

> Transform your AI agent into a research assistant capable of executing complex multi-step scientific workflows across biology, chemistry, medicine, and beyond.

> These skills enable your AI agent to seamlessly work with specialized scientific libraries, databases, and tools across multiple scientific domains. While the agent can use any Python package or API on its own, these explicitly defined skills provide curated documentation and examples that make it significantly stronger and more reliable

> Simply copy the skill folders into your skills directory and your AI agent will automatically discover and use them.

> Skills can execute code and influence your coding agent's behavior. Review what you install. [...] We run LLM-based security scans (via Cisco AI Defense Skill Scanner) on every skill in this repository.
