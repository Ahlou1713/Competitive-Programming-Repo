class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        else:
            output = []
            output.append(num // 3 - 1)
            output.append(num // 3)
            output.append(num // 3 + 1)


            return output