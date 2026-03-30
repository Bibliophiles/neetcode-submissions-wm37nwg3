class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We are treating it like a 1D matrix
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1

        while left <= right:
            middle = (left + right) // 2

            row, column = divmod(middle, len(matrix[0]))

            if target == matrix[row][column]:
                return True
            elif target > matrix[row][column]:
                left = middle + 1
            else:
                right = middle - 1

        return False
