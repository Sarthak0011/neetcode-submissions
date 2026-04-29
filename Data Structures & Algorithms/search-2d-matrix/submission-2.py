class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        N = rows * cols

        low = 0
        high = N-1

        while low <= high:
            mid = low + (high - low) // 2

            nrow = mid // cols
            ncol = mid % cols

            if matrix[nrow][ncol] == target:
                return True
            elif matrix[nrow][ncol] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False