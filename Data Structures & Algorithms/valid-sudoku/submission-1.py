class Solution:
    def _validate_row(self, board: List[List[str]], i: int, j: int) -> bool:
        n = len(board)
        for col in range(n):
            if col == j:
                continue
            if board[i][col] == board[i][j]:
                return False
        return True
    
    def _validate_column(self, board: List[List[str]], i: int, j: int) -> bool:
        n = len(board)
        for row in range(n):
            if row == i:
                continue;
            if board[row][j] == board[i][j]:
                return False
        return True
    
    def _validate_grid(self, board: List[List[str]], i: int, j: int) -> bool:
        row = (i // 3) * 3
        col = (j // 3) * 3

        for r in range(row, row+3):
            for c in range(col, col+3):
                if r == i and c == j:
                    continue
                if board[i][j] == board[r][c]:
                    return False
        return True


    def _validate_position(self, board: List[List[str]], i: int, j: int) -> bool:
        return (self._validate_row(board, i, j) 
                and self._validate_column(board, i, j) 
                and self._validate_grid(board, i, j))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for i in range(n):
            for j in range(n):
                if(board[i][j] != '.'):
                    is_valid = self._validate_position(board, i, j)
                    if not is_valid:
                        return False
        return True
        