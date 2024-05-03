class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {'(':')', '[':']', '{':'}'}
        
        for e in s:
            if e in my_dict.keys():
                stack.append(e)
            else:
                if not stack:
                    return False
                a = stack.pop()
                if e != my_dict[a]:
                    return False

        return stack == []


