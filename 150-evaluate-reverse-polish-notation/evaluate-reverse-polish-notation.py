from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isnumeric() or (token.startswith('-') and token[1:].isnumeric()):
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    # Handle division by zero
                    result = int(operand1 / operand2)
                stack.append(result)

        return stack.pop()  # Final result should be at the top of the stack
