class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """        
        rows, cols = len(matrix), len(matrix[0])
        rows_zeros, cols_zeros = [1] * rows, [1] * cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rows_zeros[r], cols_zeros[c] = 0, 0
        
        for r in range(rows):
            for c in range(cols):
                if rows_zeros[r] == 0 or cols_zeros[c] == 0:
                    matrix[r][c] = 0