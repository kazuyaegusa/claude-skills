# Acceptance Criteria + Test Harness による品質保証

> 各SkillにAcceptance Criteria(正しい/誤ったコードパターン)を定義し、Copilot SDKベースのテストハーネスで生成コードを自動検証する

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

SkillをLLMに読ませても、実際に生成されるコードが正しいとは限らない。特にimport文、認証パターン、非同期処理のバリエーションは誤りやすい。テストシナリオを用意して自動評価することで、Skillの実効性を担保できる

## いつ使うのか

Skillを追加・更新した時、生成コードの品質を機械的に保証したい時。特にimport文や認証パターンが複数ある場合(例: azure.identity の DefaultAzureCredential vs ManagedIdentityCredential)

## やり方

1. `.github/skills/<skill>/references/acceptance-criteria.md` に正しいコード例と誤ったアンチパターンを記述 2. `tests/scenarios/<skill>/scenarios.yaml` にテストケース(入力プロンプト、期待される出力、mockレスポンス)を定義 3. `cd tests && pnpm harness <skill-name> --mock --verbose` でテスト実行 4. 0-100のスコアで評価、閾値未達ならRalphループで再生成 5. CIで全スキルを自動検証

### 入力

- acceptance-criteria.md (正例/反例)
- scenarios.yaml (テストケース)
- Copilot SDK (コード生成エンジン)

### 出力

- テスト結果レポート(Pass/Fail、スコア)
- 改善が必要な箇所のフィードバック

## 使うツール・ライブラリ

- GitHub Copilot SDK
- pnpm
- test harness (カスタムスクリプト)

## コード例

```
# tests/scenarios/azure-cosmos-db-py/scenarios.yaml
scenarios:
  - name: "Basic CRUD with FastAPI"
    prompt: "Create a FastAPI endpoint to insert a document into Cosmos DB"
    expected_patterns:
      - "from azure.cosmos import CosmosClient"
      - "async def create_item"
      - "container.create_item"
    anti_patterns:
      - "import cosmos"  # 誤ったimport
      - "sync def"       # 非同期必須

# 実行
pnpm harness azure-cosmos-db-py --mock --verbose
```

## 前提知識

- AI Coding Agent(GitHub Copilot/Claude/Gemini等)の基本操作
- Git/シンボリックリンクの理解
- YAMLフロントマターの読み書き
- Azure SDK/Foundry SDK(対象ドメイン)の基礎知識
- CI/CD(GitHub Actions等)でのテスト自動化経験(テストハーネス活用時)

## 根拠

> "Ralph Loop — An iterative code generation and improvement system that: 1. Generate code 2. Evaluate against acceptance criteria 3. Analyze failures 4. Re-generate with feedback 5. Report on quality improvements"

> "128 skills with 1158 test scenarios — all skills have acceptance criteria and test scenarios."
