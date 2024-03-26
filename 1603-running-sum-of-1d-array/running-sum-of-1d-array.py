class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        output = []
        for num in nums:
            s+=num
            output.append(s)

        return output
