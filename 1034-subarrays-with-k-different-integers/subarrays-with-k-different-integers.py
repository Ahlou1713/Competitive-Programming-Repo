class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            count = 0
            left = 0
            frequency = Counter()
            
            for right in range(len(nums)):
                if frequency[nums[right]] == 0:
                    k -= 1
                frequency[nums[right]] += 1
                
                while k < 0:
                    frequency[nums[left]] -= 1
                    if frequency[nums[left]] == 0:
                        k += 1
                    left += 1
                
                count += right - left + 1
            
            return count
        
        return atMostK(nums, k) - atMostK(nums, k - 1)