class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        else:
            if k == 1:
                return 0
            else:
                new_value = str(self.kthGrammar(n-1, (k+1)//2))
                output = ''
                for s in new_value:
                    if s == '0':
                        output += '01'
                    elif s == '1':
                        output += '10'
                return int(output[(k - 1) % 2])
