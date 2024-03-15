class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if(i+1 < len(nums)):
                if(nums[i] == nums[i+1]):
                    nums[i] *= 2
                    nums[i+1] = 0

        placeholder = seeker = 0

        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[placeholder], nums[seeker] = nums[seeker], nums[placeholder]
                placeholder += 1
            seeker += 1

        return nums