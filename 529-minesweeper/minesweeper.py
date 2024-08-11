class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return []

        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        def dfs(r, c):
            if not valid(r, c) or board[r][c] != 'E':
                return

            mines = 0
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if valid(nr, nc) and board[nr][nc] == 'M':
                    mines += 1

            if mines > 0:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    dfs(nr, nc)

        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            dfs(row, col)

        return board