class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose_mat = []
        
        for j in range(len(matrix[0])):
            mat = []
            for i in range(len(matrix)):
                mat.append(matrix[i][j])
            transpose_mat.append(mat)

        return transpose_mat