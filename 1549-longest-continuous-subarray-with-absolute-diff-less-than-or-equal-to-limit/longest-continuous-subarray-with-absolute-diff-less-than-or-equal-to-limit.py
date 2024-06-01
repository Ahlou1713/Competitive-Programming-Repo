class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQue = deque() #Decreasing
        minQue = deque() #Increasing
        left = ans = 0
        for right in range(len(nums)):
            while maxQue and maxQue[-1] <nums[right]:
                maxQue.pop()
            maxQue.append(nums[right])

            while minQue and minQue[-1]>nums[right]:
                minQue.pop()
            minQue.append(nums[right])
        
            while abs(maxQue[0] - minQue[0]) > limit:
                if nums[left] == maxQue[0]:
                    maxQue.popleft()
                if nums[left] == minQue[0]:
                    minQue.popleft()
                left += 1
            ans = max(ans, right - left +1)
        return ans