class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        colors = [' ' for _ in range(numCourses)]

        def dfs(node):

            if colors[node] == 'g':
                return False

            if colors[node] == 'b':
                return True

            colors[node] = 'g'
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            colors[node] = 'b'

            return True


        for node in range(numCourses):
            if not dfs(node):
                return False

        return True
