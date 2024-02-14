class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i1 = 0
        while(i1 < len(nums)):
            i2 = i1 + 1
            while(i2 < len(nums)):
                if(nums[i1] + nums[i2] == target):
                    return [i1,i2]
                i2 += 1
            i1 += 1
    