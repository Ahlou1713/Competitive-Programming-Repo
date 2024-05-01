class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def min_max(nums):
            if len(nums) == 1 :
                return nums[0]

            return max(nums[0]-min_max(nums[1:]) , nums[-1]-min_max(nums[:-1]))
        
        return min_max(nums) >= 0