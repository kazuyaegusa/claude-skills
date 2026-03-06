#!/usr/bin/env python3
"""
マルチエージェント機能比較デモ

Claude CodeとCodexのマルチエージェント機能を
シミュレーション実行して違いを体験するデモスクリプト
"""

import asyncio
from typing import List, Dict, Any
from dataclasses import dataclass
import random
import time
from datetime import datetime


@dataclass
class TaskResult:
    """タスク実行結果"""
    agent_id: str
    task: str
    result: Any
    duration: float
    timestamp: str


class SubagentPattern:
    """1対1委譲パターンのシミュレーション"""
    
    async def delegate_task(self, task: str) -> TaskResult:
        """子エージェントにタスクを委譲"""
        start = time.time()
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        print(f"  [{timestamp}] 子エージェントに委譲: {task}")
        
        # 処理シミュレーション
        await asyncio.sleep(random.uniform(0.8, 1.2))
        
        # 処理結果の生成
        result = {
            "status": "success",
            "data": f"解析完了: {task}の構造を分析",
            "items_found": random.randint(5, 20)
        }
        
        duration = time.time() - start
        print(f"  [{timestamp}] 完了 ({duration:.2f}秒)")
        
        return TaskResult(
            agent_id="subagent-001",
            task=task,
            result=result,
            duration=duration,
            timestamp=timestamp
        )
    
    async def run(self, task: str):
        """パターン実行"""
        print(f"\n▶ Subagentパターン開始")
        result = await self.delegate_task(task)
        print(f"  結果: {result.result['data']}")
        return result


class MultiAgentsPattern:
    """並列実行パターンのシミュレーション"""
    
    async def run_agent(self, agent_id: str, task: str) -> TaskResult:
        """個別エージェントの実行"""
        start = time.time()
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        print(f"  [{timestamp}] {agent_id} 開始: {task}")
        
        # 処理時間をランダム化（並列実行のリアリティ）
        processing_time = random.uniform(0.5, 2.0)
        await asyncio.sleep(processing_time)
        
        # エージェントごとの特化処理
        if "データ" in task:
            result = {"type": "data", "records": random.randint(100, 1000)}
        elif "API" in task:
            result = {"type": "api", "endpoints": random.randint(3, 10)}
        else:
            result = {"type": "analysis", "insights": random.randint(5, 15)}
        
        duration = time.time() - start
        print(f"  [{timestamp}] {agent_id} 完了 ({duration:.2f}秒)")
        
        return TaskResult(
            agent_id=agent_id,
            task=task,
            result=result,
            duration=duration,
            timestamp=timestamp
        )
    
    async def run(self, tasks: List[str]):
        """パターン実行"""
        print(f"\n▶ Multi-Agentsパターン開始 ({len(tasks)}タスクを並列実行)")
        
        # 全タスクを並列起動
        agents = [
            self.run_agent(f"agent-{i:02d}", task) 
            for i, task in enumerate(tasks, 1)
        ]
        
        # 並列実行と結果収集
        results = await asyncio.gather(*agents)
        
        # 統計情報
        total_time = max(r.duration for r in results)
        avg_time = sum(r.duration for r in results) / len(results)
        
        print(f"  全体完了時間: {total_time:.2f}秒 (平均: {avg_time:.2f}秒)")
        print(f"  並列化による高速化: {(avg_time * len(results)) / total_time:.1f}倍")
        
        return results


class AgentTeamsPattern:
    """分散協調パターンのシミュレーション"""
    
    def __init__(self):
        self.completed_tasks = set()
        self.task_results = {}
    
    async def haiku_agent(self, task: str) -> TaskResult:
        """軽量・高速エージェント（調査タスク）"""
        start = time.time()
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        print(f"  [{timestamp}] Haiku調査: {task}")
        
        # 高速処理
        await asyncio.sleep(random.uniform(0.3, 0.6))
        
        result = {
            "agent_type": "haiku",
            "findings": f"{task}の調査結果",
            "complexity": random.choice(["低", "中", "高"])
        }
        
        duration = time.time() - start
        self.completed_tasks.add(task)
        self.task_results[task] = result
        
        print(f"  [{timestamp}] Haiku完了: {task} ({duration:.2f}秒)")
        
        return TaskResult(
            agent_id="haiku-explorer",
            task=task,
            result=result,
            duration=duration,
            timestamp=timestamp
        )
    
    async def sonnet_agent(self, task: str, dependencies: List[str]) -> TaskResult:
        """高品質エージェント（実装タスク）"""
        start = time.time()
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        print(f"  [{timestamp}] Sonnet待機中: {task} (依存: {dependencies})")
        
        # 依存タスクの完了を待機
        wait_start = time.time()
        while not all(dep in self.completed_tasks for dep in dependencies):
            await asyncio.sleep(0.1)
        
        wait_time = time.time() - wait_start
        if wait_time > 0.2:
            print(f"  [{timestamp}] Sonnet依存解決 ({wait_time:.2f}秒待機)")
        
        print(f"  [{timestamp}] Sonnet実装開始: {task}")
        
        # 高品質処理（時間をかける）
        await asyncio.sleep(random.uniform(1.0, 1.5))
        
        # 依存タスクの結果を活用
        dep_info = [self.task_results.get(d, {}) for d in dependencies]
        
        result = {
            "agent_type": "sonnet",
            "implementation": f"{task}の実装完了",
            "based_on": [d.get("findings", "") for d in dep_info],
            "quality_score": random.randint(85, 100)
        }
        
        duration = time.time() - start
        self.completed_tasks.add(task)
        
        print(f"  [{timestamp}] Sonnet完了: {task} ({duration:.2f}秒)")
        
        return TaskResult(
            agent_id="sonnet-implementer",
            task=task,
            result=result,
            duration=duration,
            timestamp=timestamp
        )
    
    async def run(self, workflow: Dict[str, Any]):
        """パターン実行"""
        print(f"\n▶ Agent Teamsパターン開始")
        print(f"  チーム編成: 調査×{len(workflow['explore'])}、実装×{len(workflow['implement'])}")
        
        tasks = []
        
        # フェーズ1: 調査タスク（Haiku）
        for task_name in workflow["explore"]:
            tasks.append(self.haiku_agent(task_name))
        
        # フェーズ2: 実装タスク（Sonnet、依存関係あり）
        for task_name in workflow["implement"]:
            deps = workflow["dependencies"].get(task_name, [])
            tasks.append(self.sonnet_agent(task_name, deps))
        
        # 全タスク実行
        results = await asyncio.gather(*tasks)
        
        # チーム統計
        total_time = max(r.duration for r in results)
        haiku_tasks = [r for r in results if r.agent_id == "haiku-explorer"]
        sonnet_tasks = [r for r in results if r.agent_id == "sonnet-implementer"]
        
        print(f"  チーム完了: {total_time:.2f}秒")
        print(f"  - Haiku平均: {sum(r.duration for r in haiku_tasks)/len(haiku_tasks):.2f}秒")
        print(f"  - Sonnet平均: {sum(r.duration for r in sonnet_tasks)/len(sonnet_tasks):.2f}秒")
        
        return results


async def main():
    """メインデモ実行"""
    
    print("=" * 60)
    print(" AI開発環境マルチエージェント機能比較デモ")
    print("=" * 60)
    print("\n各パターンの動作を実際に実行して比較します。")
    print("タイムスタンプに注目すると並列/逐次実行の違いが分かります。\n")
    
    # ========== Subagent ==========
    print("【1. Subagentパターン】")
    print("特徴: 1対1の委譲、シンプル、独立コンテキスト")
    
    subagent = SubagentPattern()
    sub_result = await subagent.run("プロジェクト構造解析")
    
    # ========== Multi-Agents ==========
    print("\n【2. Multi-Agentsパターン】")
    print("特徴: 並列実行、高速化、独立タスク")
    
    multi = MultiAgentsPattern()
    multi_tasks = [
        "データベース接続確認",
        "API仕様取得",
        "ログファイル解析"
    ]
    multi_results = await multi.run(multi_tasks)
    
    # ========== Agent Teams ==========
    print("\n【3. Agent Teamsパターン】")
    print("特徴: 分散協調、依存関係管理、複雑なワークフロー")
    
    teams = AgentTeamsPattern()
    workflow = {
        "explore": ["要件分析", "技術調査"],
        "implement": ["アーキテクチャ設計", "コア実装", "テスト作成"],
        "dependencies": {
            "アーキテクチャ設計": ["要件分析", "技術調査"],
            "コア実装": ["アーキテクチャ設計"],
            "テスト作成": ["コア実装"]
        }
    }
    team_results = await teams.run(workflow)
    
    # ========== 結果比較 ==========
    print("\n" + "=" * 60)
    print(" 実行結果の比較")
    print("=" * 60)
    
    print("\n◆ Subagent")
    print(f"  - タスク数: 1")
    print(f"  - 実行時間: {sub_result.duration:.2f}秒")
    print(f"  - 結果: {sub_result.result['items_found']}項目を発見")
    
    print("\n◆ Multi-Agents")
    print(f"  - タスク数: {len(multi_results)}")
    print(f"  - 最大実行時間: {max(r.duration for r in multi_results):.2f}秒")
    print(f"  - 並列度: 全タスクが同時実行")
    for r in multi_results:
        print(f"    - {r.task}: {r.result}")
    
    print("\n◆ Agent Teams")
    print(f"  - タスク数: {len(team_results)}")
    print(f"  - 全体実行時間: {max(r.duration for r in team_results):.2f}秒")
    print(f"  - 協調動作: 依存関係に基づく順次実行")
    for r in team_results:
        if r.agent_id == "sonnet-implementer":
            print(f"    - {r.task}: 品質スコア {r.result['quality_score']}/100")
    
    print("\n" + "=" * 60)
    print(" デモ完了")
    print("=" * 60)
    print("\n💡 ポイント:")
    print("- Subagent: シンプルで確実")
    print("- Multi-Agents: 高速並列処理")
    print("- Agent Teams: 複雑な協調作業")
    print("\n適切なパターンの選択が開発効率を大きく左右します。")


if __name__ == "__main__":
    asyncio.run(main())