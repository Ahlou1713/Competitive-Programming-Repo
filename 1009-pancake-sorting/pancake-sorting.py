class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr, end):
            start = 0
            while(start < end):
                arr[start], arr[end] = arr[end], arr[start]
                start+=1
                end-=1

        n = len(arr)
        output = []
        for i in range(n - 1, 0, -1):
            j = i
            while j > 0 and arr[j] != i + 1:
                j -= 1
            if j < i:
                if j > 0:
                    output.append(j + 1)
                    flip(arr, j)
                output.append(i + 1)
                flip(arr, i)

        return output