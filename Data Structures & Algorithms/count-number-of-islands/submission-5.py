class Solution:
    def dfs(self, grid: List[List[str]], visited: List[List[bool]], row: int, col: int) -> None:

        if visited[row][col]:
            return
        
        visited[row][col] = True

        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        n = len(grid)
        m = len(grid[0])

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == "1":
                self.dfs(grid, visited, nrow, ncol)

        

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n = len(grid)
        m = len(grid[0])

        visited = [] 
        for i in range(n):
            visited.append([False] * m)

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    self.dfs(grid, visited, i, j)
                    islands += 1
        return islands