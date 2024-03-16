class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs_columns = []
        
        for j in range(len(strs[0])):
            s = ''
            for i in range(len(strs)):
                s += strs[i][j]
            strs_columns.append(s)

        count = 0
        for str in strs_columns:
            if(sorted(list(str)) != list(str)):
                count += 1

        return count