class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == '../':
                if stack:
                    stack.pop()
            elif log == './':
                stack.append(log)
                stack.pop()
            else:
                stack.append(log)

        count = 0
        while stack:
            stack.pop()
            count += 1

        return count