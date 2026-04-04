# SKILL.md形式でドメイン知識を構造化

> Frontmatter（name/description）＋Instructions（ワークフロー・判断基準）＋References（テンプレート・チェックリスト）からなる単一Markdownファイルでエージェントの専門知識を定義する

- 出典: https://github.com/alirezarezvani/claude-skills
- 投稿者: alirezarezvani
- カテゴリ: claude-code-workflow

## なぜ使うのか

LLMは汎用的な推論は得意だが専門ドメインの手順・判断基準は持たない。SKILL.mdで「どういう順序で」「何を判断基準に」実行するかを明示すれば、エージェントは初見のタスクでも専門家レベルの実行精度を得られる

## いつ使うのか

AIエージェントに特定領域（セキュリティ、PM、マーケティング等）の作業を反復させたいとき。手順が明確で、汎用的なLLMの知識だけでは不十分な場合

## やり方

1. スキルの責務を単一ドメイン（例: セキュリティ監査）に絞る
2. Frontmatterでname/descriptionを定義
3. Instructions欄に「前提条件→手順→出力形式→エラーハンドリング」を記載
4. 必要に応じてscripts/（Pythonツール）、references/（テンプレート）、assets/（設定ファイル）を追加
5. ~/.claude/skills/{skill-name}/SKILL.md として配置

### 入力

- ドメイン専門知識（ワークフロー・チェックリスト・判断基準）
- （任意）実行用Pythonスクリプト・テンプレートファイル

### 出力

- SKILL.mdファイル（エージェントが読み込み可能）
- scripts/配下の実行可能CLIツール（依存ゼロ）

## 使うツール・ライブラリ

- テキストエディタ（VSCode等）
- Python 3.x（スクリプト作成時）
- Git（スキル管理・配布用）

## コード例

```
---
name: security-auditor
description: Scan codebase for security vulnerabilities
---

# Security Auditor Skill

## Workflow
1. Scan for hardcoded secrets (API keys, passwords)
2. Check dependency versions against CVE database
3. Analyze authentication/authorization logic
4. Generate report with severity scores

## Tools
- scripts/security_scanner.py (stdlib-only)

## Output Format
- JSON report with findings array
- Each finding: {type, severity, file, line, remediation}
```

## 前提知識

- Claude Code / Cursor / Aider 等いずれかのAIコーディングツールの基本的な使い方
- Git / GitHub の基本操作（clone, pull）
- Python 3.x の実行環境（スクリプトツール利用時）
- Bashシェルの基本知識（インストールスクリプト実行時）
- （任意）マーケティング・PM・コンプライアンス等の各ドメイン知識（該当スキル使用時）
