from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        paths = defaultdict(list)

        if destination == source:
            return True
            
        for u, v in edges:
            paths[u].append(v)
            paths[v].append(u)

        stack = [source]
        visited = set([source])

        while stack:
            node = stack.pop()
            if node == destination:
                return True

            for neighbour in paths[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)

        return False

        
