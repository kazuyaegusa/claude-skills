#!/usr/bin/env python3
"""Game Asset Generator - RPGゲーム要素自動生成スキル"""

import json
import random
import argparse
import os
from typing import Dict, List, Tuple, Optional

class GameAssetGenerator:
    """ゲームアセット生成器"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY') or os.getenv('ANTHROPIC_API_KEY')
        self.use_ai = bool(self.api_key)
    
    def create_character(self, description: str) -> Dict:
        """キャラクター生成"""
        templates = {
            "knight": {"hp": 100, "atk": 15, "def": 20, "ability": "Shield Bash"},
            "mage": {"hp": 70, "atk": 25, "def": 10, "ability": "Fireball"},
            "rogue": {"hp": 80, "atk": 20, "def": 15, "ability": "Stealth"},
            "warrior": {"hp": 120, "atk": 18, "def": 18, "ability": "Berserk"},
            "healer": {"hp": 60, "atk": 8, "def": 12, "ability": "Heal"}
        }
        
        # キーワードから職業推定
        char_type = None
        for key in templates:
            if key in description.lower():
                char_type = key
                break
        
        if not char_type:
            char_type = random.choice(list(templates.keys()))
        
        base = templates[char_type]
        
        # ステータスに10%のランダム変動
        stats = {
            k: int(v * random.uniform(0.9, 1.1)) if isinstance(v, (int, float)) else v
            for k, v in base.items()
        }
        
        return {
            "name": self._generate_name(char_type, description),
            "type": char_type,
            "description": description,
            "stats": stats,
            "backstory": self._generate_backstory(char_type)
        }
    
    def create_level(self, theme: str, size: int = 10) -> List[List[int]]:
        """レベルマップ生成"""
        level = [[0 for _ in range(size)] for _ in range(size)]
        
        # 外周を壁で囲む
        for i in range(size):
            level[0][i] = level[size-1][i] = 1
            level[i][0] = level[i][size-1] = 1
        
        # テーマ別の配置パターン
        if "dungeon" in theme.lower():
            self._add_dungeon_features(level, size)
        elif "forest" in theme.lower():
            self._add_forest_features(level, size)
        else:
            self._add_random_features(level, size)
        
        # スタートとゴール
        level[1][1] = 5  # Start
        level[size-2][size-2] = 4  # Goal
        
        return level
    
    def create_dialogue(self, context: str) -> str:
        """NPC対話生成"""
        templates = [
            "Greetings, traveler! {context}",
            "Ah, you've come at last. {context}",
            "Beware, adventurer! {context}",
            "The prophecy speaks of your arrival. {context}",
            "I've been waiting for someone like you. {context}"
        ]
        return random.choice(templates).format(context=context)
    
    def create_rpg_assets(self, theme: str) -> Dict:
        """RPGアセット一式生成"""
        hero = self.create_character(f"brave {theme} hero")
        villain = self.create_character(f"evil {theme} boss")
        level = self.create_level(theme)
        dialogue = self.create_dialogue(f"The {theme} holds many secrets")
        
        return {
            "theme": theme,
            "hero": hero,
            "villain": villain,
            "level": level,
            "dialogue": dialogue,
            "quest": self._generate_quest(theme)
        }
    
    def visualize_level(self, level: List[List[int]]) -> str:
        """レベルをASCII表示"""
        symbols = {0: ".", 1: "#", 2: "E", 3: "*", 4: "G", 5: "S"}
        return "\n".join([""."".join([symbols.get(cell, "?") for cell in row]) for row in level])
    
    def _generate_name(self, char_type: str, description: str) -> str:
        """名前生成"""
        prefixes = ["Sir", "Lady", "Lord", "The"]
        suffixes = ["the Brave", "the Bold", "the Wise", "the Strong"]
        
        if "boss" in description.lower() or "evil" in description.lower():
            return f"Dark {char_type.title()}"
        else:
            return f"{random.choice(prefixes)} {char_type.title()} {random.choice(suffixes)}"
    
    def _generate_backstory(self, char_type: str) -> str:
        """バックストーリー生成"""
        stories = {
            "knight": "Trained in the royal academy, sworn to protect the innocent.",
            "mage": "Studied the arcane arts for decades in the hidden towers.",
            "rogue": "Grew up in the shadows, mastering the art of stealth.",
            "warrior": "Forged in countless battles, seeking eternal glory.",
            "healer": "Blessed by the gods with the power to mend wounds."
        }
        return stories.get(char_type, "A mysterious figure with an unknown past.")
    
    def _generate_quest(self, theme: str) -> str:
        """クエスト生成"""
        quests = [
            f"Retrieve the ancient artifact from the {theme}",
            f"Defeat the evil lurking in the {theme}",
            f"Rescue the prisoners trapped in the {theme}",
            f"Discover the secret of the {theme}"
        ]
        return random.choice(quests)
    
    def _add_dungeon_features(self, level: List[List[int]], size: int):
        """ダンジョン要素追加"""
        # 部屋と廊下
        for _ in range(size // 3):
            x, y = random.randint(2, size-3), random.randint(2, size-3)
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 < x+dx < size-1 and 0 < y+dy < size-1:
                        level[y+dy][x+dx] = 0
        
        # 敵とアイテム
        self._add_random_features(level, size)
    
    def _add_forest_features(self, level: List[List[int]], size: int):
        """森要素追加"""
        # 木々（壁）を散在
        for _ in range(size * 2):
            x, y = random.randint(1, size-2), random.randint(1, size-2)
            if (x, y) not in [(1, 1), (size-2, size-2)]:
                level[y][x] = 1
        
        # 敵とアイテム
        self._add_random_features(level, size)
    
    def _add_random_features(self, level: List[List[int]], size: int):
        """ランダム要素追加"""
        # 敵配置
        for _ in range(size // 3):
            x, y = random.randint(1, size-2), random.randint(1, size-2)
            if level[y][x] == 0 and (x, y) not in [(1, 1), (size-2, size-2)]:
                level[y][x] = 2
        
        # アイテム配置
        for _ in range(size // 4):
            x, y = random.randint(1, size-2), random.randint(1, size-2)
            if level[y][x] == 0:
                level[y][x] = 3

def main():
    parser = argparse.ArgumentParser(description="Game Asset Generator")
    parser.add_argument("--theme", default="Dark Forest", help="Game theme")
    parser.add_argument("--themes", help="Multiple themes (comma-separated)")
    parser.add_argument("--size", type=int, default=10, help="Level size")
    parser.add_argument("--output", help="Output JSON file")
    
    args = parser.parse_args()
    
    generator = GameAssetGenerator()
    
    themes = args.themes.split(",") if args.themes else [args.theme]
    results = []
    
    for theme in themes:
        print(f"\n🎮 Generating {theme} assets...")
        assets = generator.create_rpg_assets(theme)
        results.append(assets)
        
        print(f"\n👤 Hero: {assets['hero']['name']}")
        print(f"   Type: {assets['hero']['type']}")
        print(f"   Stats: {assets['hero']['stats']}")
        
        print(f"\n👹 Villain: {assets['villain']['name']}")
        print(f"   Type: {assets['villain']['type']}")
        print(f"   Stats: {assets['villain']['stats']}")
        
        print(f"\n📜 Quest: {assets['quest']}")
        print(f"\n💬 NPC: \"{assets['dialogue']}\"")
        
        print(f"\n🗺️ Level Map:")
        print(generator.visualize_level(assets['level']))
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n✅ Saved to {args.output}")
    
    return results

if __name__ == "__main__":
    main()