class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x >= 0):
            xReverse = str(x)[::-1]
            if (str(x) == xReverse):
                return True
            else:
                return False
        else:
            return False