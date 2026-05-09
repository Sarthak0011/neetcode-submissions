class Solution:
    def dfs(self, heights: [List[List[int]]], row: int, col: int, prevHeight: int, visited: List[List[bool]]) -> None:
        if (
            row < 0 or row >= len(heights) or 
            col < 0 or col >= len(heights[0]) or
            visited[row][col] or heights[row][col] < prevHeight
        ): return

        visited[row][col] = True

        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            self.dfs(heights, nrow, ncol, heights[row][col], visited)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        m, n = len(heights), len(heights[0])

        pacific = []
        atlantic = []

        for _ in range(m):
            pacific.append([False] * n)
            atlantic.append([False] * n)

        for col in range(n):
            self.dfs(heights, 0, col, heights[0][col], pacific)
            self.dfs(heights, m-1, col, heights[m-1][col], atlantic)
        
        for row in range(m):
            self.dfs(heights, row, 0, heights[row][0], pacific)
            self.dfs(heights, row, n-1, heights[row][n-1], atlantic)
        
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        
        return res

