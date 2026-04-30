class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        islands = 0

        visited = []
        for i in range(n):
            visited_line = []
            for j in range(m):
                visited_line.append(0)
            visited.append(visited_line)

        def dfs(row, col):
            visited[row][col] = 1


            drow = [-1, 0, 1, 0]
            dcol = [0, 1, 0, -1]

            for i in range(4):
                nrow = drow[i] + row
                ncol = dcol[i] + col

                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == "1" and not visited[nrow][ncol]:
                    dfs(nrow, ncol)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    islands += 1

        return islands