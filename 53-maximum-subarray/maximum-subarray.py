class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = maxim = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], nums[i]+curr)
            maxim = max(curr, maxim)

        
        return maxim