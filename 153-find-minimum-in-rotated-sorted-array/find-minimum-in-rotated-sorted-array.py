class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        minimum = nums[right]

        while left <= right:
            mid = left + (right-left) // 2

            if nums[mid] <= nums[right]:
                minimum = min(minimum, nums[mid])
                right = mid - 1
            else:
                left = mid + 1

        return minimum