from collections import deque
from dataclasses import dataclass
from time import perf_counter
from typing import Optional

@dataclass
class SolveResult:
    path: list[tuple[Optional[str],tuple[int]]]
    expanded:int
    elapsed_ms:float
    solution_count:int

def bfs(start,is_goal,moves):
    started=perf_counter()
    queue=deque([start])
    distance={start:0}
    ways={start:1}
    parents={}
    expanded=0

    while queue:
        state=queue.popleft()
        if is_goal(state):
            path=[]
            current=state
            while current!=start:
                previous,action=parents[current]
                path.append((action,current))
                current=previous
            path.append((None,start))
            path.reverse()
            return SolveResult(
                path,expanded,(perf_counter()-started)*1000,ways[state]
            )

        expanded+=1
        next_distance=distance[state]+1
        for action,next_state in moves(state):
            if next_state not in distance:
                distance[next_state]=next_distance
                ways[next_state]=ways[state]
                parents[next_state]=(state,action)
                queue.append(next_state)
            elif distance[next_state]==next_distance:
                ways[next_state]+=ways[state]

    return None