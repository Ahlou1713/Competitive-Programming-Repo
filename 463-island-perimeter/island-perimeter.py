class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # perimeter = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             perimeter += 4
        #             if i > 0 and grid[i-1][j] == 1:
        #                 perimeter -= 2
        #             if j > 0 and grid[i][j-1] == 1:
        #                 perimeter -= 2
        # return perimeter

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(grid, visited, row, col):
            # base case
            visited[row][col] = True

            perimeter = 4
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and grid[new_row][new_col]:
                    perimeter -= 1
                    if not visited[new_row][new_col]:
                        perimeter += dfs(grid, visited, new_row, new_col)

            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])) :
                if grid[i][j]:
                    return dfs(grid, visited, i, j)
        
        return 0

