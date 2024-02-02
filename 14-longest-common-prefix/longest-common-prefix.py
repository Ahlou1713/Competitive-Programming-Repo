class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 1):
            return strs[0]
        commonPrefix = ''
        i = 0
        while(i<=len(strs[0])):
            prefix = strs[0][:i]
            b = 1
            for str in strs:
                if not (str.startswith(prefix)):
                    b = 0
            if (b == 1):
                commonPrefix = prefix
            i += 1
                    
    
        return commonPrefix        
        