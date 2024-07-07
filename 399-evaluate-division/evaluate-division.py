class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)

        for i in range(n):
            a, b =  equations[i]
            weight = values[i]

            graph[a].append((b,weight))
            graph[b].append((a,1/weight))
        
        output = []
        visited = set()

        def dfs(node, end):
            visited.add(node)
            
            if node == end: 
                return 1.0
            
            for neighbour, weight in graph[node]:
                if neighbour not in visited:
                    tmp = dfs(neighbour, end)
                    if tmp != -1.0 :
                        return weight * tmp
            

            return -1.0


        for start, end in queries : 
            if start not in graph or end not in graph:
                output.append(-1)
                continue
            
            output.append(dfs(start, end))
            visited.clear()
        
        return output
        