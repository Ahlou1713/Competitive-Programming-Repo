class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            if target >= matrix[i][0] and target <= matrix[i][m-1]:

                left = 0
                right = m-1

                while left <= right:
                    mid = left + (right-left) // 2

                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1

        return False