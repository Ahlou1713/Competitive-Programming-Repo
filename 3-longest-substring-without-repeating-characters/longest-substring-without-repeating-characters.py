class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        dic = defaultdict(int)
        max_len = 0
        for right in range(len(s)):
            dic[s[right]] += 1
            while left < len(s) and len(dic) != (right-left+1):
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1
            max_len = max(max_len, right-left+1)

        return max_len