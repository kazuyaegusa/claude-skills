#!/usr/bin/env python3
"""
マルチエージェントシステム デモ
"""

import asyncio
from multi_agent import StarPatternExecutor, DistributedExecutor

async def main():
    print("=" * 60)
    print("マルチエージェントシステム デモンストレーション")
    print("=" * 60)
    
    # サンプルタスク生成
    tasks = [
        {'id': f'task_{i}', 'type': f'type_{["A","B","C"][i%3]}', 
         'data': f'データ{i+1}'}
        for i in range(9)
    ]
    
    # スター型実行
    print("\n【スター型アーキテクチャ】")
    star_executor = StarPatternExecutor()
    star_results, star_time = await star_executor.execute(tasks, num_agents=3)
    
    print(f"  処理時間: {star_time:.3f}秒")
    print(f"  並列度: {len(tasks)/star_time:.1f}タスク/秒")
    
    # 分散型実行
    print("\n【分散型アーキテクチャ】")
    capabilities_map = {
        "agent_1": {"type_A", "type_B"},
        "agent_2": {"type_B", "type_C"},
        "agent_3": {"type_C", "type_A"}
    }
    
    dist_executor = DistributedExecutor()
    dist_results, dist_time = await dist_executor.execute(
        tasks, capabilities_map
    )
    
    print(f"  処理時間: {dist_time:.3f}秒")
    print(f"  並列度: {len(tasks)/dist_time:.1f}タスク/秒")
    
    # 比較
    print("\n【パフォーマンス比較】")
    if star_time < dist_time:
        improvement = ((dist_time - star_time) / dist_time) * 100
        print(f"  → スター型が{improvement:.1f}%高速")
    else:
        improvement = ((star_time - dist_time) / star_time) * 100
        print(f"  → 分散型が{improvement:.1f}%高速")
    
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())