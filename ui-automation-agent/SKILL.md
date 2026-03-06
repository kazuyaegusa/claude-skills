---
name: UI Automation Agent
description: 画面UIを解析してクリック・入力を自動化するエージェント
commands:
  - ui-automate
---

# UI Automation Agent

画面HTML/UIを解析してインタラクション可能な要素を検出し、タスク指示からアクション列を計画・実行する。

## 使い方

```bash
# スクリプトとして使用
python ui_automation_agent.py
```

```python
from ui_automation_agent import CUAgent

agent = CUAgent()
result = agent.execute_task(
    task="フォームに名前を入力して送信",
    screen_html="<form><input name='name'><button>送信</button></form>"
)
```

## 機能

- **VisionAnalyzer**: HTML/UIから操作可能要素を検出（ボタン、入力フィールド、リンク）
- **TaskPlanner**: タスク指示から実行アクション列を生成
- **BrowserExecutor**: アクション列をブラウザ操作に変換（Playwright/Selenium連携可能）

## 依存パッケージ

基本動作には標準ライブラリのみ使用。実際のブラウザ操作には以下が必要：

```
playwright>=1.40.0
selenium>=4.15.0
```

## ユースケース

- Webフォーム自動入力
- UI操作の自動化テスト
- スクレイピング補助
- RPAタスク自動化

## 注意事項

- 現在のExecutorはモック実装。実際のブラウザ操作にはPlaywright/Selenium統合が必要
- Vision解析は正規表現ベース。実際のAI Vision APIと連携可能
