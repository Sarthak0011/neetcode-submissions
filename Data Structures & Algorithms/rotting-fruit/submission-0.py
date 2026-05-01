class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[0] * m for _ in range(n)]

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i, j, 0])
                    visited[i][j] = 1
                elif grid[i][j] == 0:
                    visited[i][j] = 1

        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        time = 0
        while q:
            r, c, t = q.popleft()

            time = max(time, t)

            for i in range(4):
                nrow = drow[i] + r
                ncol = dcol[i] + c

                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == 1 and not visited[nrow][ncol]:
                    q.append([nrow, ncol, t+1])
                    visited[nrow][ncol] = 1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    return -1
        
        return time



