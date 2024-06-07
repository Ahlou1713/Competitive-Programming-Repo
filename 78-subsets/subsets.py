class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curr = []

        def backtrack(firstnum):
            subsets.append(curr[:])

            for i in range(firstnum, len(nums)):
                # if (i > firstnum and nums[i] == nums[i-1]): continue
                curr.append(nums[i])
                backtrack(i + 1)   
                curr.pop()  

            return

        backtrack(0)
        return subsets      