class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        visited = []
        for _ in range(m): 
            visited.append([False] * n)
        
        q = deque()

        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0 or row == m-1 or col == n-1:
                    if board[row][col] == 'O' and not visited[row][col]:
                        q.append([row, col])
                        visited[row][col] = True
        
        while q:
            row, col = q.popleft()

            drow = [-1, 0, 1, 0]
            dcol = [0, 1, 0, -1]

            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]
                
                if (
                    nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and
                    board[nrow][ncol] == 'O' and not visited[nrow][ncol]
                ):
                    q.append([nrow, ncol])
                    visited[nrow][ncol] = True

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'









