class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        heap = []
        
        for num in nums2:
            heapq.heappush(heap, (num + nums1[0], 0))
        
        while k > 0 and heap:
            _sum, index = heapq.heappop(heap)
            result.append([nums1[index], _sum - nums1[index]])
            
            if index + 1 < len(nums1):
                heapq.heappush(heap, (_sum - nums1[index] + nums1[index + 1], index + 1))
            
            k -= 1
        
        return result