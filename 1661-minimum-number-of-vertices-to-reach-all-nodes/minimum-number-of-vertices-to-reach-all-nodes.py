class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegree = [0] * n

        for _, to in edges:
            indegree[to] += 1

        output = []
        for i in range(n):
            if indegree[i] == 0:
                output.append(i)

        return output