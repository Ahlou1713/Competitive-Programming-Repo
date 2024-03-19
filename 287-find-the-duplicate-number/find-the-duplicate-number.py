class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        for x in nums:
            if (cnt[x] > 1):
                return x