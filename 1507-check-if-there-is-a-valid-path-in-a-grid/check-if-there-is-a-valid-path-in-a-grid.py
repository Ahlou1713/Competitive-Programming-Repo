class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        n, m = len(grid), len(grid[0])

        directions = {1: [(0,-1), (0,1)], 2: [(1,0), (-1,0)], 3: [(0,-1), (1,0)], 4: [(0,1), (1,0)], 5: [(0,-1), (-1,0)], 6: [(0,1), (-1,0)]}

        queue = deque([(0, 0)])
        visited = set((0, 0))

        while queue:
            x, y = queue.popleft()
            if x == n-1 and y == m-1:
                return True

            for dx, dy in directions[grid[x][y]]:
                newx = x+dx
                newy = y+dy
                if 0 <= newx < n and 0 <= newy < m and (newx, newy) not in visited:
                    if (-dx,-dy) in directions[grid[newx][newy]]:
                        queue.append((newx, newy))
                        visited.add((newx, newy))
                        
        return False