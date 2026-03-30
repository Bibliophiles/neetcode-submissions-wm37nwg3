class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count = len(matrix)
        column_count = len(matrix[0])
        # We are treating it like a 1D matrix
        left = 0
        right = (row_count * column_count) - 1

        while left <= right:
            middle = (left + right) // 2

            row, column = divmod(middle, column_count)

            if target == matrix[row][column]:
                return True
            elif target > matrix[row][column]:
                left = middle + 1
            else:
                right = middle - 1

        return False
