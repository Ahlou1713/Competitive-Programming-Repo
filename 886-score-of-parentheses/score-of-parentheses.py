class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0

        for i, e in enumerate(s):
            if e == '(':
                stack.append(i)  
            elif e == ')':
                if stack[-1] == i - 1: 
                    stack.pop() 
                    score += 2 ** (len(stack))  
                else:
                    stack.pop()

        return score
