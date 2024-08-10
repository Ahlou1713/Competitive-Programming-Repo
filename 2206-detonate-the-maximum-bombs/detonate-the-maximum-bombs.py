class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        dictio = defaultdict(set)
        n = len(bombs)

        for i in range(n):  
            xi, yi, ri = bombs[i]

            for j in range(n):
                if i == j:
                    continue

                xj, yj, rj = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:  
                    dictio[i].add(j)

        def dfs(n, visited):  
            if n in visited:
                return
            visited.add(n)
            for neighbour in dictio[n]:
                dfs(neighbour, visited)

        ans = 0
        for i in range(n):
            visited = set()
            dfs(i, visited)
            ans = max(ans, len(visited))
            
        return ans