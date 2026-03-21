# Ralph Loop による反復改善

> 生成→評価→フィードバック→再生成を繰り返し、品質閾値(例: 85点)に達するまでコードを改善し続ける

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

1回の生成で完璧なコードが出るとは限らない。特にAcceptance Criteriaが厳しい場合、複数回の試行が必要。Ralphループは失敗理由をLLMに返して次の生成に活かすため、手動リトライより効率的

## いつ使うのか

新しいSkillを作成した時、既存Skillを大幅更新した時。特にAcceptance Criteriaが複雑で、1回の生成では満たせない時

## やり方

1. Skillとシナリオを指定してコード生成 2. Acceptance Criteriaでスコアリング(0-100) 3. スコアが閾値未満なら、失敗理由(欠けているimport、誤った関数呼び出し等)をLLMフィードバック用に整形 4. フィードバック付きでプロンプトを再構築し、再生成 5. max-iterations回まで繰り返し、最終スコアをレポート 6. `pnpm harness <skill> --ralph --max-iterations 5 --threshold 85` で実行

### 入力

- Skill YAML frontmatter + 本文
- scenarios.yaml
- max-iterations (デフォルト3)
- threshold (目標スコア、デフォルト80)

### 出力

- 各iteration毎のスコア推移
- 最終生成コード
- 改善レポート

## 使うツール・ライブラリ

- Copilot SDK (生成)
- カスタム評価ロジック (スコアリング)
- フィードバック生成ロジック

## コード例

```
# Ralph Loopでazure-ai-projects-pyを改善
pnpm harness azure-ai-projects-py --ralph --mock --max-iterations 5 --threshold 85

# 出力例:
# Iteration 1: Score 65 (missing async import)
# Iteration 2: Score 78 (wrong credential type)
# Iteration 3: Score 88 (PASS)
# Final: 88/100
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
