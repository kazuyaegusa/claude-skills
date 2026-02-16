# スキル修正計画

Anthropic公式ベストプラクティス（2026-02時点）に基づく、カスタムスキル8件の監査結果と修正タスク。

**参照**: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

---

## 監査サマリー

| スキル | 重要度 | 主な問題 |
|--------|--------|----------|
| quality-harness | **高** | 770行（上限500行超過）→ 分割必須 |
| phase-report | **高** | YAMLフロントマター完全欠落 |
| pdf-logo-remover | **中** | ハードコードパス + `user_invocable` 欠落 |
| project-review | **中** | 非標準フロントマター + `user_invocable` 欠落 |
| everything-claude-code-ja | **低** | description に "when to use" 不足 |
| repo-tracker | **低** | macOS限定のスケジュール記述 |
| discord-context-search | **適合** | 修正不要 |
| folder-digest | **適合** | 修正不要 |

---

## 1. quality-harness（重要度: 高）

### 問題
- SKILL.md が **770行**（推奨上限500行を大幅超過）
- 全テンプレート・grader定義が1ファイルに詰め込まれている
- プログレッシブディスクロージャー未適用

### 修正タスク
1. SKILL.md を概要+ナビゲーション（~150行以内）に縮小
2. 以下の参照ファイルに分割:
   - `reference/templates.md` — eval/runner テンプレート定義
   - `reference/graders.md` — 4種のgrader（ExactMatch, Contains, KeyExists, Schema）仕様
   - `reference/ci-cd.md` — GitHub Actions / Git hooks 設定
   - `reference/makefile.md` — Makefile テンプレート
3. SKILL.md に各参照ファイルへのリンクを記載（1段階の深さを厳守）

### 修正例（SKILL.mdの構造）
```markdown
---
name: quality-harness
description: 任意のPythonプロジェクトに品質ハーネスを一括セットアップする。evalテストケース定義、実行隔離、CI/CD、Git hooksを導入。Pythonプロジェクトの品質基盤構築時に使用。
user_invocable: true
---

# Quality Harness

## クイックスタート
[基本的な使い方を記載]

## 詳細リファレンス
- **テンプレート定義**: [reference/templates.md](reference/templates.md)
- **Grader仕様**: [reference/graders.md](reference/graders.md)
- **CI/CD設定**: [reference/ci-cd.md](reference/ci-cd.md)
- **Makefile**: [reference/makefile.md](reference/makefile.md)
```

---

## 2. phase-report（重要度: 高）

### 問題
- **YAMLフロントマターが完全に欠落**（`name`, `description` なし）
- Claudeがスキル発見時にメタデータを読めず、正しくトリガーされない可能性
- `user_invocable: true` も未設定

### 修正タスク
1. YAMLフロントマターを追加:
```yaml
---
name: phase-report
description: フェーズ完了レポートを自動生成し、gitコミット・プッシュまで完全自動実行する。プロジェクトのフェーズ区切りでレポートを作成したい時に使用。
user_invocable: true
---
```
2. ファイル先頭の `# フェーズ完了レポート自動生成` の前に上記を挿入

---

## 3. pdf-logo-remover（重要度: 中）

### 問題
- スクリプトパスが **`/Users/kazuyaegusa/`** にハードコード（他デバイスで動かない）
- `user_invocable: true` が未設定
- ベストプラクティス: 相対パスまたはスキルディレクトリ相対で記述すべき

### 修正タスク
1. `user_invocable: true` をフロントマターに追加
2. ハードコードパスを相対パスに変更:
```diff
- `/Users/kazuyaegusa/.claude/skills/pdf-logo-remover/remove_pdf_logo.py`
+ `remove_pdf_logo.py`（このスキルディレクトリ内）
```
3. 使い方セクションのコマンド例も相対パス化:
```markdown
## 使い方
python3 scripts/remove_pdf_logo.py input.pdf
# または
python3 ~/.claude/skills/pdf-logo-remover/remove_pdf_logo.py input.pdf
```

---

## 4. project-review（重要度: 中）

### 問題
- フロントマターに非標準フィールド `command`, `arguments` が含まれている
- `user_invocable: true` が未設定
- `description` に "when to use" トリガー文言が不足

### 修正タスク
1. 非標準フィールドを削除し、`user_invocable: true` を追加
2. `description` を改善（what + when to use）:
```yaml
---
name: project-review
description: プロジェクトのドキュメント・コードを多角的にレビューし、実現性・正確性・改善点を検証して修正する。プロジェクトの品質レビューやブラッシュアップ時に使用。
user_invocable: true
---
```

---

## 5. everything-claude-code-ja（重要度: 低）

### 問題
- `description` に "when to use" が不足（何をするかは書いてあるが、いつ使うかが不明確）
- `user_invocable` が未設定
- 本体22行で内容が薄い（ただし参照ファイルへの誘導はベストプラクティスに沿っている）

### 修正タスク
1. `description` を改善:
```yaml
---
name: everything-claude-code-ja
description: Everything Claude Codeの使い方を日本語で案内する。Claude Codeの導入・運用・注意点を知りたい時や、機能について日本語で質問された時に使用。
user_invocable: true
---
```
2. SKILL.md本体に、参照ファイルの内容概要を少し追加（目次的な役割）

---

## 6. repo-tracker（重要度: 低）

### 問題
- スケジュール設定が macOS (launchd) のみ対応
- Linux (cron/systemd) での代替手順がない

### 修正タスク
1. スケジュール設定セクションにLinux対応を追加:
```markdown
### macOS (launchd)
/repo-tracker install-schedule

### Linux (cron)
crontab -e
# 以下を追加:
*/30 * * * * cd ~/.repo-tracker && python3 ~/.claude/skills/repo-tracker/repo_tracker.py check-all
```
2. エラーハンドリングの明確化（ネットワークエラー時の挙動を記述）

---

## 7. discord-context-search（修正不要）

フロントマター適合、行数適切（131行）、プログレッシブディスクロージャー不要。

---

## 8. folder-digest（修正不要）

フロントマター適合、行数適切（103行）、プログレッシブディスクロージャー不要。

---

## 共通改善事項（全スキル対象）

### description の書き方統一
- 三人称で記述（「〜する」形式）
- 「what + when to use」を必ず含める
- 1024文字以内

### テスト
- 各スキルについて最低3つの評価シナリオを作成（将来タスク）
- Haiku/Sonnet/Opus での動作確認（将来タスク）

---

## 実装優先順位

1. **phase-report**: フロントマター追加（5分で完了、効果大）
2. **pdf-logo-remover**: パス修正 + user_invocable追加（10分）
3. **project-review**: フロントマター修正（5分）
4. **quality-harness**: ファイル分割（30分〜1時間、最も作業量が多い）
5. **everything-claude-code-ja**: description改善（5分）
6. **repo-tracker**: Linux対応追加（15分）

---

*作成日: 2026-02-16*
*参照: Anthropic Skills Best Practices (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)*
