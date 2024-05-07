class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for e in s:
            if stack and e == '*':
                stack.pop()
            elif e == '*':
                continue
            else:
                stack.append(e)
        
        return ''.join(stack)