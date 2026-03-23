# セキュリティツールチェーンをLLMで自律オーケストレーションする

> Semgrep（静的解析）→CodeQL（データフロー検証）→AFL（ファジング）→LLM分析→PoC生成→パッチ提案を一貫してエージェントが自動実行

- 出典: https://github.com/gadievron/raptor
- 投稿者: gadievron
- カテゴリ: claude-code-workflow

## なぜ使うのか

従来はツール間の連携が手動で、脆弱性検証やPoC生成に専門知識が必要。LLMがツール出力を解釈して次のアクションを決定することで、エンドツーエンドの自動化が可能になる

## いつ使うのか

セキュリティスキャンから修正までを自動化したい時、既存ツールチェーンをLLMで統合したい時

## やり方

1. /scanコマンドでSemgrep+CodeQLを実行
2. LLMが検出結果をImpact×Exploitability/DetectionTimeで優先度付け
3. /codeqlで高優先度の脆弱性をデータフロー分析で検証
4. /exploitで検証済み脆弱性のPoC（コンパイル可能なC/Python）を生成
5. /patchでセキュアな修正案を生成
6. /fuzzでバイナリファジング（AFL++）を実行し、クラッシュを再現
7. 全結果を構造化レポート（JSON/Markdown）で出力

### 入力

- ソースコードまたはバイナリ
- セキュリティポリシー（Semgrep rules、CodeQL queries）

### 出力

- 優先度付き脆弱性リスト
- 検証済みPoC
- 修正パッチ案
- 構造化レポート

## 使うツール・ライブラリ

- Semgrep
- CodeQL
- AFL++
- LiteLLM

## コード例

```
# Claude Code command sequence
/scan --repo /path/to/code --policy_groups secrets
# → LLM analyzes findings, prioritizes by Impact×Exploitability/DetectionTime
/codeql --finding CVE-2024-XXXX
# → Dataflow validation with CodeQL
/exploit --finding CVE-2024-XXXX
# → Generate compilable PoC
/patch --finding CVE-2024-XXXX
# → Generate secure patch
```

## 前提知識

- Claude Codeの基本操作（コマンド、スキル、エージェントの概念）
- セキュリティツールの基礎知識（Semgrep、CodeQL、AFL、ペネトレーションテスト）
- LLMプロバイダのAPI認証（ANTHROPIC_API_KEY等）
- BigQuery認証（OSS Forensics使用時）
- Dockerまたはdevcontainer環境構築（オプション）
