#!/usr/bin/env python3
"""
マルチエージェントシステム実装
"""

import asyncio
import time
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Set
from dataclasses import dataclass
import random

@dataclass
class Message:
    sender_id: str
    recipient_id: str
    content: Any
    timestamp: float

class BaseAgent(ABC):
    def __init__(self, agent_id: str, role: str):
        self.agent_id = agent_id
        self.role = role
        self.inbox = asyncio.Queue()
        self.results = []

    @abstractmethod
    async def process_task(self, task: Dict[str, Any]) -> Any:
        pass

    async def send_message(self, recipient: 'BaseAgent', content: Any):
        message = Message(
            sender_id=self.agent_id,
            recipient_id=recipient.agent_id,
            content=content,
            timestamp=time.time()
        )
        await recipient.inbox.put(message)

# === スター型実装 ===
class ParentAgent(BaseAgent):
    def __init__(self):
        super().__init__("parent", "coordinator")
        self.children = []

    def add_child(self, child: 'ChildAgent'):
        self.children.append(child)

    async def distribute_tasks(self, tasks: List[Dict[str, Any]]):
        futures = []
        for i, task in enumerate(tasks):
            child = self.children[i % len(self.children)]
            future = asyncio.create_task(child.process_task(task))
            futures.append(future)
        
        results = await asyncio.gather(*futures)
        return results

    async def process_task(self, task: Dict[str, Any]) -> Any:
        subtasks = task.get('subtasks', [task])
        return await self.distribute_tasks(subtasks)

class ChildAgent(BaseAgent):
    def __init__(self, agent_id: str, specialization: str, process_func=None):
        super().__init__(agent_id, specialization)
        self.process_func = process_func

    async def process_task(self, task: Dict[str, Any]) -> Any:
        if self.process_func:
            return await self.process_func(task)
        
        # デフォルト処理
        processing_time = random.uniform(0.05, 0.15)
        await asyncio.sleep(processing_time)
        
        return {
            'agent_id': self.agent_id,
            'task_id': task.get('id', 'unknown'),
            'processing_time': processing_time,
            'result': f"Processed {task.get('data', '')}"
        }

# === 分散型実装 ===
class TaskList:
    def __init__(self):
        self.tasks = asyncio.Queue()
        self.completed = []
        self.lock = asyncio.Lock()

    async def add_task(self, task: Dict[str, Any]):
        await self.tasks.put(task)

    async def get_task(self) -> Optional[Dict[str, Any]]:
        try:
            return await asyncio.wait_for(self.tasks.get(), timeout=0.1)
        except asyncio.TimeoutError:
            return None

    async def mark_completed(self, task_id: str, result: Any):
        async with self.lock:
            self.completed.append({
                'task_id': task_id,
                'result': result,
                'timestamp': time.time()
            })

class TeamAgent(BaseAgent):
    def __init__(self, agent_id: str, capabilities: Set[str], process_func=None):
        super().__init__(agent_id, "team_member")
        self.capabilities = capabilities
        self.task_list = None
        self.processed_count = 0
        self.process_func = process_func

    def join_team(self, task_list: TaskList):
        self.task_list = task_list

    async def collaborate(self):
        while True:
            task = await self.task_list.get_task()
            if not task:
                break
            
            if task.get('type') in self.capabilities:
                if self.process_func:
                    result = await self.process_func(task)
                else:
                    processing_time = random.uniform(0.05, 0.15)
                    await asyncio.sleep(processing_time)
                    result = f"{self.agent_id} completed {task.get('type')}"
                
                await self.task_list.mark_completed(task['id'], result)
                self.processed_count += 1
            else:
                # 処理できない場合は戻す
                await self.task_list.add_task(task)
        
        return self.processed_count

# === 実行制御 ===
class StarPatternExecutor:
    async def execute(self, tasks: List[Dict[str, Any]], 
                     num_agents: int = 3,
                     process_funcs: Optional[List] = None) -> tuple:
        parent = ParentAgent()
        
        for i in range(num_agents):
            process_func = process_funcs[i] if process_funcs else None
            child = ChildAgent(f"child_{i+1}", f"specialty_{i+1}", process_func)
            parent.add_child(child)
        
        start_time = time.time()
        results = await parent.process_task({'subtasks': tasks})
        elapsed = time.time() - start_time
        
        return results, elapsed

class DistributedExecutor:
    async def execute(self, tasks: List[Dict[str, Any]], 
                     capabilities_map: Dict[str, Set[str]],
                     process_funcs: Optional[Dict] = None) -> tuple:
        task_list = TaskList()
        
        for task in tasks:
            await task_list.add_task(task)
        
        agents = []
        for agent_id, capabilities in capabilities_map.items():
            process_func = process_funcs.get(agent_id) if process_funcs else None
            agent = TeamAgent(agent_id, capabilities, process_func)
            agent.join_team(task_list)
            agents.append(agent)
        
        start_time = time.time()
        await asyncio.gather(*[agent.collaborate() for agent in agents])
        elapsed = time.time() - start_time
        
        return task_list.completed, elapsed