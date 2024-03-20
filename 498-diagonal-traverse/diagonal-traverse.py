class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        if(m == 0 or n == 0):
            return []
        arr = []
        row = col = 0
        up = True

        while(row<m and col<n):
            if(up):
                while(row>0 and col<n-1):
                    arr.append(mat[row][col])
                    row-=1
                    col+=1
                arr.append(mat[row][col])
                if(col == n-1):
                    row+=1
                else:
                    col+=1
            else:
                while(col>0 and row<m-1):
                    arr.append(mat[row][col])
                    col-=1
                    row+=1
                arr.append(mat[row][col])
                if(row == m-1):
                    col+=1
                else:
                    row+=1
            up = not up
        
        return arr