class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = 0
        while (i < len(s)):
            b = True
            j = 0
            while (j < len(s) and b):
                if(i != j):
                    if(s[i] == s[j]):
                        b = False
                j += 1
            if(b):
                return i
            i += 1
        return -1