# uvパッケージマネージャでスキル依存関係管理

> 各スキルのPython依存関係をuvで高速インストール・管理し、環境構築を自動化する

- 出典: https://github.com/K-Dense-AI/claude-scientific-skills
- 投稿者: K-Dense-AI
- カテゴリ: claude-code-workflow

## なぜ使うのか

科学計算ライブラリは依存関係が複雑だが、uvはpipより高速で再現性が高い。スキル単位で依存を明示することで、必要なパッケージだけインストール可能。

## いつ使うのか

新しいスキルを使い始める時、または依存パッケージのバージョン管理が必要な時

## やり方

1. uvをインストール（curl -LsSf https://astral.sh/uv/install.sh | sh）
2. 各スキルのSKILL.mdで必要パッケージを確認
3. uv pip install <package-name>で依存をインストール
4. エージェントが自動的にスキル実行時に依存を検出・インストール（設定による）

### 入力

- SKILL.mdファイル（依存パッケージ記載）
- Python 3.11+環境

### 出力

- インストール済み依存パッケージ
- 再現可能な実行環境

## 使うツール・ライブラリ

- uv (https://docs.astral.sh/uv/)

## コード例

```
# uvインストール（macOS/Linux）
curl -LsSf https://astral.sh/uv/install.sh | sh

# パッケージインストール
uv pip install scanpy rdkit pytorch-lightning
```

## 前提知識

- Agent Skills標準に対応したAIエージェント（Cursor / Claude Code / Codex / Gemini CLI等）の基本操作
- Python 3.11+の実行環境
- uvパッケージマネージャの基礎知識
- 科学計算の基本概念（ゲノミクス・化学・機械学習等、使用する分野の基礎）
- 各スキルが対象とする科学ライブラリ・データベースの概要理解（詳細はSKILL.mdで補完可能）

## 根拠

> Skills can execute code and influence your coding agent's behavior. Review what you install. [...] We run LLM-based security scans (via Cisco AI Defense Skill Scanner) on every skill in this repository.

> The skills use uv as the package manager for installing Python dependencies.
