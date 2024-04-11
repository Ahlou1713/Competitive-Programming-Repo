class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        check_if_palindrome = lambda s: s == s[::-1]
        
        def checkCondition(a: str, b: str) -> bool:
            left, right = 0, len(a) - 1
            while left < right and a[left] == b[right]:
                left += 1; right -= 1
            return check_if_palindrome(a[left: right + 1]) or check_if_palindrome(b[left: right + 1])
        
        return checkCondition(a, b) or checkCondition(b, a)