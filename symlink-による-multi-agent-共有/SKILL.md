# symlink による Multi-Agent 共有

> `.github/skills/` を正とし、`.claude/skills`, `.opencode/skills` 等へsymlinkを張ることで、複数Agent設定間でSkillを共有する

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

同じリポジトリで複数のAI Agentを使う場合、Skillを各Agent用にコピーするとメンテナンスが煩雑になる。symlinkなら一箇所を更新すれば全Agentに反映される

## いつ使うのか

Copilot/Claude/Gemini等を1つのリポジトリで併用する時、Skillを重複管理したくない時

## やり方

1. `.github/skills/` 配下に正式版Skillを配置 2. `ln -s ../.github/skills .claude/skills` でClaude用ディレクトリへリンク 3. `ln -s ../.github/skills .opencode/skills` でOpenCode用ディレクトリへリンク 4. 各AgentのAGENTS.mdやcopilot-instructions.mdで `skills/` を参照 5. 更新は `.github/skills/` で一元管理

### 入力

- 正式版Skill置き場(`.github/skills/`)
- 各Agentの設定ディレクトリ(`.claude/`, `.opencode/`)

### 出力

- symlink
- 全Agent共通のSkill参照環境

## 使うツール・ライブラリ

- ln -s

## コード例

```
# .github/skills/を正とする
ln -s ../.github/skills .claude/skills
ln -s ../.github/skills .opencode/skills

# .claude/CLAUDE.md で参照
# "Skills are located in .claude/skills/"
```

## 前提知識

- AI Coding Agent(GitHub Copilot/Claude/Gemini等)の基本操作
- Git/シンボリックリンクの理解
- YAMLフロントマターの読み書き
- Azure SDK/Foundry SDK(対象ドメイン)の基礎知識
- CI/CD(GitHub Actions等)でのテスト自動化経験(テストハーネス活用時)

## 根拠

> "132 skills in `.github/skills/` — flat structure with language suffixes for automatic discovery"
