class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        curr = []

        def backtrack(firstnum):
            if len(curr) == k:
                combinations.append(curr[:])
                return

            for num in range(firstnum, n+1):
                curr.append(num)
                backtrack(num + 1)   
                curr.pop()  

        backtrack(1)
        return combinations      