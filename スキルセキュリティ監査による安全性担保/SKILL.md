# スキルセキュリティ監査による安全性担保

> skill-security-auditor を使って、インストール前にスキルのコード・指示内容をスキャンし、コマンドインジェクション、コード実行、データ流出等のリスクを検出する

- 出典: https://github.com/alirezarezvani/claude-skills
- 投稿者: alirezarezvani
- カテゴリ: claude-code-workflow

## なぜ使うのか

サードパーティ製スキルには悪意あるコード・プロンプトインジェクションが含まれる可能性があり、盲目的にインストールするとセキュリティリスクとなる

## いつ使うのか

外部ソースからスキルをインストールする前、または社内で作成したスキルを本番環境に展開する前

## やり方

1. python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/ を実行
2. PASS / WARN / FAIL の判定と、検出された問題の詳細を確認
3. FAIL の場合は修正案に従ってスキルを改修または利用を中止
4. WARN の場合はリスクを理解した上で使用判断

### 入力

- スキルディレクトリのパス
- （スキル内の SKILL.md, scripts/, references/ 等）

### 出力

- セキュリティ判定（PASS/WARN/FAIL）
- 検出された脆弱性の詳細リスト
- 修正推奨事項

## 使うツール・ライブラリ

- Python標準ライブラリ（依存なし）

## コード例

```
python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py \
  ~/.claude/skills/external-skill/

# 出力例
# FAIL: Command injection risk detected in scripts/deploy.py:42
# Remediation: Use subprocess with shell=False and validate inputs
```

## 前提知識

- Claude CodeまたはOpenAI Codex等のAIコーディングツールの基本的な使い方
- SKILL.md形式やエージェント概念の理解（ただしREADMEに説明あり）
- Bash/シェルスクリプトの基本知識（インストールスクリプト実行用）
- Python 3.x の実行環境（CLIツール使用時）
- Git/GitHub の基本操作
