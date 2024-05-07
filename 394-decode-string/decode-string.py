class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curr_str = ''
        
        for e in s:
            if e.isdigit():
                num = num * 10 + int(e)
            elif e == '[':
                stack.append(curr_str)
                stack.append(num)
                curr_str = ''
                num = 0
            elif e == ']':
                prev_num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + prev_num * curr_str
            else:
                curr_str += e
        
        return curr_str


                

                