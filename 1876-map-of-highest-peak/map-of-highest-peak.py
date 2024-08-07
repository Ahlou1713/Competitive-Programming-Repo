class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        n, m = len(isWater), len(isWater[0])
        result = [row[:] for row in isWater]
        visited = set()
        queue = deque()

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    visited.add((i, j))
                    queue.append((i, j, 0))

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while queue:
            row, col, height = queue.popleft()

            for rOff, cOff in directions:
                next_row, next_col = row + rOff, col + cOff

                if 0 <= next_row < n and 0 <= next_col < m and (next_row, next_col) not in visited:
                    result[next_row][next_col] = height + 1
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col, height + 1))

        return result