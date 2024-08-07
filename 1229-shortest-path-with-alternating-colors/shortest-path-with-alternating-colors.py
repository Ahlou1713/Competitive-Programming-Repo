from collections import deque, defaultdict
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        queue = deque([(0, 0, 0), (0, 1, 0)])
        graph = defaultdict(lambda: defaultdict(list))

        for u, v in redEdges:
            graph[u][0].append(v)  

        for u, v in blueEdges:
            graph[u][1].append(v) 

        visited = [[False, False] for _ in range(n)]
        ans = [-1] * n

        while queue:
            index, colour, length = queue.popleft()

            if visited[index][colour]: 
                continue

            visited[index][colour] = True

            if ans[index] == -1: 
                ans[index] = length

            for neighbour in graph[index][colour]:
                nextcolour = 1 - colour
                if not visited[neighbour][nextcolour]:
                    queue.append((neighbour, nextcolour, length + 1))

        return ans
