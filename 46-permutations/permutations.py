class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        curr = []

        def backtrack():
            if len(curr) == len(nums):
                permutations.append(curr[:])
                return

            for i in range(len(nums)):
                if nums[i] in curr: continue
                curr.append(nums[i])
                backtrack()   
                curr.pop()  

        backtrack()
        return permutations