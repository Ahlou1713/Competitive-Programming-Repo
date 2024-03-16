class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = ans = 0
        nums.sort()

        for i in range(1, len(nums)): 
            if nums[i-1] < nums[i]: 
                count += 1
            ans += count
        return ans  