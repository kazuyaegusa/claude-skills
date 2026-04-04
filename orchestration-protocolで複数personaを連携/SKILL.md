# Orchestration Protocolで複数Personaを連携

> Solo Sprint（フェーズごとにPersona切替）、Domain Deep-Dive（1 Persona + 複数スキル）、Multi-Agent Handoff（Persona間レビュー）、Skill Chain（Personaなし・スキルのみ連鎖）の4パターンでタスクを分解・割り当てる

- 出典: https://github.com/alirezarezvani/claude-skills
- 投稿者: alirezarezvani
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一のPersona/スキルでは完結しない作業（例: 製品ローンチ = 設計＋開発＋マーケティング＋分析）を、複数のPersona/スキルに分割して並行または順次実行することで、各領域の専門性を最大化しつつ全体を完遂できる

## いつ使うのか

6週間の製品ローンチ、コンプライアンス監査＋実装、マルチチャネルマーケティングキャンペーンなど、複数領域にまたがる大規模タスク

## やり方

1. タスク全体を分析し、必要なドメイン（Engineering/Marketing/Product等）を特定
2. 各ドメインに対応するPersonaまたはスキルを選定
3. 依存関係に基づいてパターンを選択:
   - 並列可能→Solo Sprint or Multi-Agent Handoff
   - 順次実行→Skill Chain
   - 深掘り→Domain Deep-Dive
4. orchestration/ORCHESTRATION.md のテンプレートに従って実行計画を記述
5. エージェントに「Week 1-2: startup-cto + aws-solution-architect」等の指示を与える

### 入力

- タスクの全体像（ゴール・制約・期限）
- 利用可能なPersona/スキル一覧
- 依存関係グラフ（どの作業が他の作業に依存するか）

### 出力

- Orchestration計画書（Markdown）
- 各フェーズの成果物（ADR、レポート、実装等）

## 使うツール・ライブラリ

- orchestration/ORCHESTRATION.md テンプレート
- Personaファイル群
- SKILL.mdファイル群

## コード例

```
# 6-Week Product Launch Orchestration

## Phase 1: Architecture (Week 1-2)
- Persona: startup-cto
- Skills: senior-architect, aws-solution-architect, senior-frontend
- Deliverable: ADR + Infrastructure plan

## Phase 2: Marketing Prep (Week 3-4)
- Persona: growth-marketer
- Skills: launch-strategy, copywriting, seo-audit
- Deliverable: Launch page + Email sequence

## Phase 3: Ship & Iterate (Week 5-6)
- Persona: solo-founder
- Skills: email-sequence, analytics-tracking
- Deliverable: Live product + metrics dashboard

## Handoff Points
- Week 2 → Week 3: ADR review by growth-marketer (validate marketing feasibility)
- Week 4 → Week 5: Launch page review by startup-cto (validate tech claims)
```

## 前提知識

- Claude Code / Cursor / Aider 等いずれかのAIコーディングツールの基本的な使い方
- Git / GitHub の基本操作（clone, pull）
- Python 3.x の実行環境（スクリプトツール利用時）
- Bashシェルの基本知識（インストールスクリプト実行時）
- （任意）マーケティング・PM・コンプライアンス等の各ドメイン知識（該当スキル使用時）

## 根拠

> skill-security-auditor — Security gate — scan skills for malicious code before installation. Scans for: command injection, code execution, data exfiltration, prompt injection, dependency supply chain risks, privilege escalation. Returns PASS / WARN / FAIL with remediation guidance. Zero dependencies.

> Personas go beyond 'use these skills' — they define how an agent thinks, prioritizes, and communicates.

> Orchestration: A lightweight protocol for coordinating personas, skills, and agents on work that crosses domain boundaries. Four patterns: Solo Sprint, Domain Deep-Dive, Multi-Agent Handoff, Skill Chain
