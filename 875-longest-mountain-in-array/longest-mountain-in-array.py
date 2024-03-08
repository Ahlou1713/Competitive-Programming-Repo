class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
    
        ans = 0
        i = 1
        while i <= n - 2:
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                count = 0
                # now we find the index where a peak is present
                j = i # making a temporary element to help us traverse the array using two pointer techniques
                while j > 0 and arr[j] > arr[j - 1]:
                    count += 1
                    j -= 1
                while i <= n - 2 and arr[i] > arr[i + 1]:
                    count += 1
                    i += 1
                ans = max(ans, count)
            else:
                i += 1
        if ans > 0:
            return ans + 1
        return ans