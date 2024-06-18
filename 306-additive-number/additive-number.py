class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        current = []
       
        def backtrack(idx):
            if idx >= len(num):
                for i in range(2, len(current)):
                    if current[i - 2] + current[i - 1] != current[i]:
                        return False
                return len(current) > 2
            
            for i in range(idx, len(num)):
                val = num[idx:i+1]
                if len(val) > 1 and val[0] == '0':
                    continue
                val = int(num[idx:i+1])
                current.append(val)
                if len(current) < 3 or current[-1] == current[-2] + current[-3]:
                    if backtrack(i + 1):
                        return True
                current.pop()

            return False

        return backtrack(0)


            