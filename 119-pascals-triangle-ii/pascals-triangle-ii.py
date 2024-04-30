class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        return self.prefixSumModified(self.getRow(rowIndex-1))

    def prefixSumModified(self, arr: List[int]) -> List[int]:
        n = len(arr)
        new_arr = [0] * (n + 1)
        new_arr[0] = arr[0]
        i = 1
        while i < n:
            new_arr[i] = arr[i - 1] + arr[i]
            i += 1
        new_arr[i] = 1
        print(new_arr)
        return new_arr
