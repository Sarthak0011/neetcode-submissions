class Pair:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        n = len(grid)
        m = len(grid[0])

        visited = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(0)
            visited.append(temp)

        def bfs(row, col):
            q = deque([Pair(row, col)])
            visited[row][col] = 1

            drow = [-1, 0, 1, 0]
            dcol = [0, 1, 0, -1]

            while q:
                
                p = q.popleft()
                r = p.row
                c = p.col

                for i in range(4):
                    nrow = drow[i] + r
                    ncol = dcol[i] + c

                    if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == "1" and not visited[nrow][ncol]:
                        q.append(Pair(nrow, ncol))
                        visited[nrow][ncol] = 1

        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    islands += 1

        return islands

        