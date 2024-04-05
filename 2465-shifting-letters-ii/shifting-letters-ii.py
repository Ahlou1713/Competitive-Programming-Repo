class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        '''
        s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
        list = [97, 98, 99]
        p = [0, 0, 0, 0]
        p = [-1, 0, 1, 0]
        p = [-1, 1, 1, -1]
        p = [0, 1, 1, -2]
        p = [0, 1, 2, 0]
        '''
        arr = [0] * (n+1)
        m = len(shifts)
        for i in range(m):
            if shifts[i][2] == 0:
                arr[shifts[i][0]] -= 1
                arr[shifts[i][1] + 1] +=1
            elif shifts[i][2] == 1:
                arr[shifts[i][0]] += 1
                arr[shifts[i][1] + 1] -=1
        
        for i in range(1, n):
            arr[i] += arr[i-1]

        new_str = ''
        i = 0
        for l in s:
            ord_l = (ord(l) - ord('a') + arr[i]) % 26 + ord('a')
            new_str += chr(ord_l)
            i += 1

        return new_str