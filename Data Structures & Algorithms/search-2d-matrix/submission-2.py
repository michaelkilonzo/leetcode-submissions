class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on matrix to find row 
        row_l, row_r = 0, len(matrix) - 1
        while row_l <= row_r:
            row_m = (row_l + row_r) // 2
            if target == matrix[row_m][-1]:
                return True
            if target > matrix[row_m][-1]:
                row_l = row_m + 1
            else:
                row_r = row_m - 1 
    
        if row_l >= len(matrix):
            return False

        # binary search on row_l to find target 
        l, r = 0, len(matrix[row_l]) - 1
        while l <= r: 
            m = (l + r) // 2
            if target == matrix[row_l][m]:
                return True
            if target > matrix[row_l][m]:
                l = m + 1 
            else:
                r = m - 1

        return False