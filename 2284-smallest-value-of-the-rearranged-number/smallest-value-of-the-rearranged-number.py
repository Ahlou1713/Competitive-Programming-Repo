class Solution:
    def smallestNumber(self, num: int) -> int:
        
        if (num == 0):
            return 0

        is_negative = False
        nums = []
        count_zero = 0
        s = str(num)

        if num < 0:
            is_negative = True
            s = s[1:]
        
        n = len(s)
        for i in range(n):
            if s[i] != '0':
                nums.append(s[i])
            else:
                count_zero += 1

        nums.sort(reverse=is_negative)
        new_str = ''.join(nums)

        if is_negative:
            return int('-' + new_str + '0'*count_zero)

        return int(new_str[0] + '0'*count_zero + new_str[1:])

