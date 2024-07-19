class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        arr = []
        arr.extend([1] * numOnes)
        arr.extend([0] * numZeros)
        arr.extend([-1] * numNegOnes)

        return sum(arr[:k])