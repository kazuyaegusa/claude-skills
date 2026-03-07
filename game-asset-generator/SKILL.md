---
name: Game Asset Generator
author: Claude
version: 1.0.0
description: RPGゲームのキャラクター、レベルマップ、NPCダイアログを自動生成
tags: [game-dev, rpg, procedural-generation, level-design]
---

# Game Asset Generator

RPGゲームの基本要素を自動生成するスキル。キャラクター設定、レベルマップ、NPCダイアログなどを統合的に生成。

## 機能

- **キャラクター生成**: ヒーロー/ボスのステータス、能力、バックストーリー
- **レベルマップ生成**: 2Dグリッドベースのマップ（壁、敵、アイテム配置）
- **ダイアログ生成**: NPC会話テンプレート
- **ASCII可視化**: レベルマップをテキストで表示

## 使用方法

```python
from game_asset_generator import GameAssetGenerator

generator = GameAssetGenerator()

# テーマベースでゲームアセット一式生成
assets = generator.create_rpg_assets("Dark Forest")

# 個別生成も可能
hero = generator.create_character("brave knight")
level = generator.create_level("dungeon", size=15)
dialogue = generator.create_dialogue("The dragon awaits")

# レベル可視化
print(generator.visualize_level(level))
```

## 依存パッケージ

```bash
pip install openai anthropic  # LLM統合時のみ
```

## コマンド実行

```bash
# デモ実行
python game_asset_generator.py --theme "Sky Temple"

# 複数テーマ生成
python game_asset_generator.py --themes "Forest,Cave,Castle"
```

## 出力例

```
🎮 Theme: Dark Forest
👤 Hero: The Knight
   Stats: HP=100, ATK=15, DEF=20
   Ability: Shield Bash
👹 Boss: The Dark Lord
   Stats: HP=150, ATK=25, DEF=15
💬 NPC: "Beware, adventurer! The Dark Forest is dangerous"
🗺️ Level Map:
##########
#S.....E.#
#..#.....#
#..*..#..#
#....E...#
#.#......#
#..E..*..#
#........#
#.......G#
##########
```

## カスタマイズ

LLM統合で高度な生成が可能：

```python
class AdvancedGenerator(GameAssetGenerator):
    def __init__(self, api_key=None):
        super().__init__()
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        
    def generate_with_ai(self, prompt):
        # GPT-4/Claude APIで高品質生成
        pass
```