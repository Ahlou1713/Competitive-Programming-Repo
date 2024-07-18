class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] * k
        minUnfairness = sum(cookies)
       
        def backtrack(i, bucket):
            nonlocal minUnfairness
            if i == len(cookies):
                minUnfairness = min(minUnfairness, max(bucket))
                return
           
            for j in range(k):
                bucket[j] += cookies[i]
                backtrack(i+1, bucket)
                bucket[j] -= cookies[i]
                if bucket[j] == 0:
                    break
       
        backtrack(0, bucket)
        return minUnfairness