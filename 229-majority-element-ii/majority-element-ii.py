class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majE = []
        for num in nums:
            if(nums.count(num) > len(nums) / 3):
                majE.append(num)
        return set(majE)