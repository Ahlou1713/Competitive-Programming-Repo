class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]

        new_str = ''
        i = 0
        for l in s:
            ord_l = (ord(l) - ord('a') + shifts[i]) % 26 + ord('a')
            new_str += chr(ord_l)
            i+=1

        return new_str
        