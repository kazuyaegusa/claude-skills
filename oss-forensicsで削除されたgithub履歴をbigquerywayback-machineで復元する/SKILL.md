# OSS Forensicsで削除されたGitHub履歴をBigQuery+Wayback Machineで復元する

> /oss-forensicsコマンドでGitHub Archive（BigQuery）、Wayback Machine、ローカルgit履歴から証拠を収集し、削除されたコミット・イシュー・リポジトリを復元

- 出典: https://github.com/gadievron/raptor
- 投稿者: gadievron
- カテゴリ: claude-code-workflow

## なぜ使うのか

セキュリティインシデント調査では、攻撃者が証拠隠滅のために履歴を削除することが多い。不変なGH Archiveと外部アーカイブから復元することで、改ざんされていない証拠を取得できる

## いつ使うのか

GitHubリポジトリのセキュリティインシデント調査、削除された履歴の復元、証拠ベースの帰属分析が必要な時

## やり方

1. /oss-forensicsコマンドでリポジトリURLを指定
2. 並列で証拠収集（GH Archive via BigQuery、GitHub API、Wayback Machine、ローカルgit）
3. 削除されたコミット・イシューをタイムスタンプ付きで復元
4. ベンダーレポートからIOC（Indicators of Compromise）を自動抽出
5. 証拠をオリジナルソースに対して検証
6. LLMが証拠ベースの仮説を生成・反復改善
7. タイムライン・帰属・IOCを含む詳細レポート出力

### 入力

- GitHubリポジトリURL
- ベンダーレポート（オプション）
- GOOGLE_APPLICATION_CREDENTIALS（BigQuery認証用）

### 出力

- 復元された削除履歴
- IOCリスト
- 証拠ベースの帰属仮説
- タイムライン付き調査レポート

## 使うツール・ライブラリ

- GH Archive（BigQuery）
- GitHub API
- Wayback Machine
- git

## コード例

```
# Claude Code
/oss-forensics --repo https://github.com/victim/compromised-repo
# → Multi-agent orchestration:
#   1. Evidence collection (parallel): GH Archive, GitHub API, Wayback, local git
#   2. Deleted content recovery
#   3. IOC extraction from vendor reports
#   4. Evidence verification
#   5. Hypothesis formation (iterative refinement)
#   6. Forensic reporting
```

## 前提知識

- Claude Codeの基本操作（コマンド、スキル、エージェントの概念）
- セキュリティツールの基礎知識（Semgrep、CodeQL、AFL、ペネトレーションテスト）
- LLMプロバイダのAPI認証（ANTHROPIC_API_KEY等）
- BigQuery認証（OSS Forensics使用時）
- Dockerまたはdevcontainer環境構築（オプション）

## 根拠

> OSS Forensics: Evidence Collection via GH Archive, GitHub API, Wayback Machine, local git... Deleted Content Recovery... IOC Extraction... Evidence Verification... Hypothesis Formation
