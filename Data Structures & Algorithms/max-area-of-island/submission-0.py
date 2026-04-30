class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        m = len(grid[0])

        visited = [[0] * m for _ in range(n)]
        max_area = 0
        def bfs(row, col):
            visited[row][col] = 1
            area = 1

            drow = [-1, 0, 1, 0]
            dcol = [0, 1, 0, -1]

            q = deque([[row, col]])

            while q:
                r, c = q.popleft()

                for i in range(4):
                    nrow = drow[i] + r
                    ncol = dcol[i] + c

                    if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] and not visited[nrow][ncol]:
                        q.append([nrow, ncol])
                        visited[nrow][ncol] = 1
                        area += 1
            return area

        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not visited[i][j]:
                    area = bfs(i, j)
                    max_area = max(max_area, area)
        return max_area