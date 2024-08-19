class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        curr_num = 0
        for num in nums:
            if num == 1:
                curr_num += 1
                max_num = max(max_num, curr_num)
            else:
                curr_num = 0

        return max_num