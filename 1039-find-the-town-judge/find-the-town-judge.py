class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        indegree = [0] * n
        outdegree = [0] * n

        for a, b in trust:
            outdegree[a-1] += 1
            indegree[b-1] += 1

        for person in range(1, n+1):
            if outdegree[person-1] == 0 and indegree[person-1] == n-1:
                return person
        
        return -1

