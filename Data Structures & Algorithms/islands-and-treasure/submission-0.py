class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append([i, j])
        
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        while q:
            r, c = q.popleft()

            for i in range(4):
                nrow = drow[i] + r
                ncol = dcol[i] + c

                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == 2147483647:
                    grid[nrow][ncol] = grid[r][c] + 1
                    q.append([nrow, ncol])

        

        
        