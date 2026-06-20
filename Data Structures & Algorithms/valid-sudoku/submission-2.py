class Solution:
    def __checkGrid(self, board: List[List[str]], row: int, col: int) -> bool:
        curr = board[row][col]
        grid_start_row = (row // 3) * 3
        grid_start_col = (col // 3) * 3

        for i in range(grid_start_row, grid_start_row+3):
            for j in range(grid_start_col, grid_start_col+3):
                if i == row and j == col:
                    continue
                if board[i][j] == curr:
                    return False
        return True

    def __checkCol(self, board: List[List[str]], row: int, col: int) -> bool:
        curr = board[row][col]
        for i in range(len(board)):
            if i != row and board[i][col] == curr:
                return False
        return True

    def __checkRow(self, board: List[List[str]], row: int, col: int) -> bool:
        curr = board[row][col]
        for i in range(len(board)):
            if i != col and board[row][i] == curr:
                return False
        return True


    def __isValid(self, board: List[List[str]], i: int, j: int) -> bool:
        return self.__checkRow(board, i, j) and self.__checkCol(board, i, j) and self.__checkGrid(board, i, j)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    if not self.__isValid(board, i, j):
                        return False
        return True