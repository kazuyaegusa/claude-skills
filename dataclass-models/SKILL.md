---
title: Dataclass Models Pattern
description: dataclassを使った型安全なデータモデル定義パターン
tags: [dataclass, models, python, typing]
---

# Dataclass Models Pattern

Python dataclassを使用した型安全なデータモデル定義パターン。

## 基本的なモデル定義

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
import json

@dataclass
class BaseModel:
    """基底モデルクラス"""
    id: int
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: Optional[str] = None
    
    def to_dict(self) -> dict:
        """辞書変換"""
        return {
            k: v for k, v in self.__dict__.items()
            if v is not None
        }
    
    def to_json(self) -> str:
        """JSON変換"""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)
    
    @classmethod
    def from_dict(cls, data: dict):
        """辞書から生成"""
        return cls(**data)

@dataclass
class User(BaseModel):
    """ユーザーモデル"""
    name: str
    email: str
    is_active: bool = True
    tags: List[str] = field(default_factory=list)

@dataclass
class Post(BaseModel):
    """投稿モデル"""
    title: str
    content: str
    author_id: int
    published: bool = False
    view_count: int = 0
    tags: List[str] = field(default_factory=list)
    
    def publish(self):
        """公開処理"""
        self.published = True
        self.updated_at = datetime.now().isoformat()
```

## 使用例

```python
# モデル生成
user = User(
    id=1,
    name="Alice",
    email="alice@example.com",
    tags=["admin", "verified"]
)

post = Post(
    id=100,
    title="Hello World",
    content="This is my first post",
    author_id=user.id
)

# メソッド呼び出し
post.publish()

# 変換
print(post.to_json())
post_dict = post.to_dict()

# 復元
restored_post = Post.from_dict(post_dict)
```

## 応用: ネスト構造

```python
@dataclass
class Comment:
    """コメントモデル（ネスト対応）"""
    id: int
    text: str
    author: str
    replies: List['Comment'] = field(default_factory=list)
    
    def add_reply(self, reply: 'Comment'):
        self.replies.append(reply)
    
    def count_all_replies(self) -> int:
        """全返信数をカウント（再帰）"""
        count = len(self.replies)
        for reply in self.replies:
            count += reply.count_all_replies()
        return count
```

## 特徴

- 型ヒント付きで IDE サポート充実
- デフォルト値と factory 関数サポート
- 自動的な __init__, __repr__, __eq__ 生成
- 継承可能で拡張性が高い
- JSON/辞書との相互変換が簡単