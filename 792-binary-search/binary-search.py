class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        high = 0
        low = n

        while high < low:
            mid = high + (low-high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                low = mid
            else:
                high = mid + 1

        return -1