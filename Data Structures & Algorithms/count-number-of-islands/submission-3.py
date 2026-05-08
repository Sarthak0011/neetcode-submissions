class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = []
        for i in range(n):
            visited.append([False] * m)
        
        def bfs(row, col):
            q = deque()
            q.append([row, col])

            drow = [-1, 0, 1, 0]
            dcol = [0, 1, 0, -1]

            while q:
                r, c = q.popleft()
                visited[r][c] = True

                for i in range(4):
                    nrow = r + drow[i]
                    ncol = c + dcol[i]

                    if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == '1' and not visited[nrow][ncol]:
                        q.append([nrow, ncol])
        
        def dfs(row, col):
            visited[row][col] = True

            drow = [-1, 0, 1, 0]
            dcol = [0, 1, 0, -1]

            for i in range(4):
                nrow = drow[i] + row
                ncol = dcol[i] + col

                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == '1' and not visited[nrow][ncol]:
                    dfs(nrow, ncol)


        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    # bfs(i, j)
                    dfs(i, j)
                    islands += 1
        
        return islands

