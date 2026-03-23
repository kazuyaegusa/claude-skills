# スキルをコレクション形式で配布する

> 複数のスキルを1つのリポジトリにまとめ、`npx`やインストールスクリプト経由で一括導入できるようにする

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

個別にスキルをインストールするのは手間がかかる。コレクションとしてパッケージ化すれば、1コマンドで数十のスキルを導入でき、即座に生産性が向上する

## いつ使うのか

特定の用途（フルスタック開発、PM業務、セキュリティ監査等）に必要なスキル一式を配布したい時、チームで標準環境をセットアップしたい時

## やり方

1. 関連するスキルを1つのGitHubリポジトリに格納（例: superpowers, OpenPaw, Agent Almanac）
2. `package.json`でnpxエントリーポイントを定義、またはインストールスクリプトを提供
3. ユーザーは`npx pawmode`等のコマンドで全スキルを`~/.claude/skills/`にコピー
4. Claude Code起動時、全スキルが自動的に利用可能になる

### 入力

- スキルファイル群（SKILL.md）
- インストールスクリプトまたはnpxエントリーポイント

### 出力

- 1コマンドでインストール可能なスキルバンドル
- ユーザーの`~/.claude/skills/`にコピーされた全スキル

## 使うツール・ライブラリ

- npm/npx
- GitHub
- OpenPaw (38 skills)
- Agent Almanac (317 skills)

## コード例

```
# Install OpenPaw skill bundle
npx pawmode
# All 38 skills are now in ~/.claude/skills/
```

## 前提知識

- Claude Codeの基本的な使い方（プロンプト実行、ツール呼び出し）
- GitHubリポジトリのクローン・PRの基本操作
- SKILL.mdの配置場所（`~/.claude/skills/`）の理解
- （MCPスキル使用時）Model Context Protocolの概念とサーバーインストール方法

## 根拠

> 「A curated list of Claude Skills」

> 「100以上のスキルリンク（docx, pdf, test-driven-development, VibeSec-Skill, aws-skills, postgres, linear-claude-skill等）」

> 「[Tip] If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked」

> 「Collections: OpenPaw (38 skills), Agent Almanac (317 skills), agentskill.sh (69,000+ skills)」
