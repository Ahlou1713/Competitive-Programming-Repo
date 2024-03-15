class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        target_arr = []
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if(sorted_nums[i] == target):
                target_arr.append(i)

        return target_arr