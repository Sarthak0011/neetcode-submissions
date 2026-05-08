class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        m = len(grid)
        n = len(grid[0])

        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])

        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        while q:
            row, col = q.popleft()
            
            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]

                if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and grid[nrow][ncol] == INF:
                    q.append([nrow, ncol])
                    grid[nrow][ncol] = grid[row][col] + 1
        
    