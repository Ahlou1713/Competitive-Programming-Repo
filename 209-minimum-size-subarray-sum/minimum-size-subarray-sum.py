class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        min_output = len(nums)
        left = 0
        right = 0
        summ = 0
        while(right<n):
            summ+=nums[right]

            while(summ>=target):
                summ-=nums[left]
                min_output = min(min_output, right-left+1)
                left+=1

            right+=1

        if(sum(nums) < target):
            return 0
        else:
            return min_output
