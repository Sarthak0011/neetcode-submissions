class Solution {
    private boolean checkRow(char[][] board, int i, int j) {
        char element = board[i][j];
        for(int it = 0; it < board.length; it++) {
            if(it == j) continue;
            if(board[i][it] == element) return false;
        }
        return true;
    }
    private boolean checkCol(char[][] board, int i, int j) {
        char element = board[i][j];
        for(int it = 0; it < board.length; it++) {
            if(it == i) continue;
            if(board[it][j] == element) return false;
        }
        return true;
    }
    private boolean checkGrid(char[][] board, int i, int j) {
        char element = board[i][j];
        int startRow = (i / 3) * 3;
        int startCol = (j / 3) * 3;

        for(int row = startRow; row < startRow+3; row++) {
            for(int col = startCol; col < startCol+3; col++) {
                if(row == i && col == j) continue;
                if(board[row][col] == element) return false;
            }
        }
        return true;
    }
    private boolean validatePosition(char[][] board, int i, int j) {
        return checkRow(board, i, j) && checkCol(board, i, j) && checkGrid(board, i, j);
    }
    public boolean isValidSudoku(char[][] board) {
        int n = board.length;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(board[i][j] == '.') continue;
                boolean isValid = validatePosition(board, i, j);
                if(!isValid) return false;
            }
        }

        return true;
    }
}
