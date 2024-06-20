class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()

        def isValid(r, c):
            return 0 <= r < n and 0 <= c < m and not (r,c) in visited

        def dfs(r, c):

            visited.add((r, c))

            for rOff, cOff in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                rNew, cNew = r+rOff, c+cOff

                if isValid(rNew, cNew) and grid[rNew][cNew] == '1':
                    dfs(rNew, cNew)

        output = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1' and isValid(r,c):
                    output += 1
                    dfs(r, c)

        return output 