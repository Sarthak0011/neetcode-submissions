class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = []

        for _ in range(m):
            visited.append([False] * n)

        def dfs(row, col):
            visited[row][col] = True

            drow = [-1, 0, 1, 0]
            dcol = [0, 1, 0, -1]
            area = 1
            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]

                if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and grid[nrow][ncol] and not visited[nrow][ncol]:
                    area += dfs(nrow, ncol)
            return area
        
        def bfs(row, col):
            q = deque()
            q.append([row, col])
            area = 1
            visited[row][col] = True

            drow = [-1, 0, 1, 0]
            dcol = [0, 1, 0, -1]

            while q:
                r, c = q.popleft()

                for i in range(4):
                    nrow = r + drow[i]
                    ncol = c + dcol[i]

                    if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and grid[nrow][ncol] and not visited[nrow][ncol]:
                        visited[nrow][ncol] = True
                        area += 1
                        q.append([nrow, ncol])
            return area
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    # curr_area = dfs(i, j)
                    curr_area = bfs(i, j)
                    if curr_area > max_area: max_area = curr_area
        return max_area

