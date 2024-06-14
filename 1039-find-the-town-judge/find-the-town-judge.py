from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

        trusts = defaultdict(lambda: [0, 0])

        for a, b in trust:
            trusts[a][0] += 1
            trusts[b][1] += 1

        for person in range(1, n+1):
            if trusts[person] == [0,n-1]:
                return person
        
        return -1

