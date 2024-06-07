class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        curr = []

        def backtrack(firstnum):

            if sum(curr) == target:
                output.append(curr[:])
                return
            elif sum(curr) > target:
                return

            for i in range(firstnum, len(candidates)):
                curr.append(candidates[i])
                backtrack(i)   
                curr.pop() 

        backtrack(0)
        return output