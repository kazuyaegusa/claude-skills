---
title: SQLite Storage Pattern
description: SQLiteを使った簡単なCRUD操作とデータ永続化パターン
tags: [database, sqlite, python, storage]
---

# SQLite Storage Pattern

SQLiteを使用した軽量なデータ永続化パターン。

## 基本的な使い方

```python
import sqlite3
from pathlib import Path
from typing import Optional, Any

class Storage:
    def __init__(self, db_path: str = "data.db"):
        self.db_path = Path(db_path)
        self._init_db()
    
    def _init_db(self):
        """テーブル初期化"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    value TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
    
    def insert(self, name: str, value: str) -> int:
        """データ挿入"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO items (name, value) VALUES (?, ?)",
                (name, value)
            )
            conn.commit()
            return cursor.lastrowid
    
    def get(self, item_id: int) -> Optional[dict]:
        """データ取得"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT * FROM items WHERE id = ?",
                (item_id,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def update(self, item_id: int, **kwargs):
        """データ更新"""
        fields = ", ".join([f"{k} = ?" for k in kwargs.keys()])
        values = list(kwargs.values()) + [item_id]
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                f"UPDATE items SET {fields} WHERE id = ?",
                values
            )
            conn.commit()
    
    def search(self, query: str) -> list[dict]:
        """検索"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT * FROM items WHERE name LIKE ?",
                (f"%{query}%",)
            )
            return [dict(row) for row in cursor.fetchall()]
```

## 使用例

```python
# ストレージ初期化
storage = Storage("myapp.db")

# データ挿入
item_id = storage.insert("example", "value123")

# データ取得
item = storage.get(item_id)
print(item)  # {'id': 1, 'name': 'example', 'value': 'value123', ...}

# データ更新
storage.update(item_id, value="new_value")

# 検索
results = storage.search("exam")
```

## 特徴

- ファイルベースで設定不要
- Python標準ライブラリのみで動作
- トランザクション自動管理
- Row Factory で辞書形式の結果取得