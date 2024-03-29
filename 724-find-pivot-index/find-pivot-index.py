class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n

        left_sum[0] = nums[0]
        for j in range(1, n):
            left_sum[j] = left_sum[j-1] + nums[j]

        right_sum[n-1] = nums[n-1]
        for j in range(n-2,-1,-1):
            right_sum[j] = right_sum[j+1] + nums[j]
        
        for i in range(n):
            if left_sum[i] == right_sum[i]:
                return i

        return -1
