class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)

        for i in range(k, len(nums)):
            heappushpop(heap, nums[i])


        return heappop(heap)