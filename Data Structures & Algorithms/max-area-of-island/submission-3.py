class Solution:
    def bfs(self, grid: List[List[int]], visited: List[List[bool]], row: int, col: int) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()
        q.append([row, col])
        visited[row][col] = True

        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        area = 0

        while q:
            r, c = q.popleft()
            area += 1

            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]

                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == 1 and not visited[nrow][ncol]:
                    q.append([nrow, ncol])
                    visited[nrow][ncol] = True
        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()

        max_area = 0

        visited = []
        for i in range(n):
            visited.append([False] * m)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = self.bfs(grid, visited, i, j)
                    max_area = max(max_area, area)
        return max_area