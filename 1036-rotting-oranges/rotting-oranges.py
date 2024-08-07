class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        output = 0

        while queue:
            i, j, minute = queue.popleft()
            for iOff, jOff in directions:
                new_i, new_j = i + iOff, j + jOff
                if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == 1:
                    grid[new_i][new_j] = 2
                    queue.append((new_i, new_j, minute+1))
                    output = max(output, minute+1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return output