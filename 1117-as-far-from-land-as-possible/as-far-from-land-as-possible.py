class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        output = -1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    queue.append((i, j, 0))

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while queue:
            row, col, steps = queue.popleft()

            for rOff, cOff in directions:
                next_row, next_col = row + rOff, col + cOff

                if 0 <= next_row < n and 0 <= next_col < m and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
                    output = max(output, steps+1)


        return output