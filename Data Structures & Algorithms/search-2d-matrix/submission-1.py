class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count = len(matrix)
        column_count = len(matrix[0])

        total_number_in_matrix = row_count * column_count
        left = 0
        right = total_number_in_matrix - 1
        
        while left <= right:
            middle = (left + right) // 2
            row_index = middle // column_count
            column_index = middle % column_count

            mid_num = matrix[row_index][column_index]
            if target == mid_num:
                return True
            elif target < mid_num:
                right = middle - 1
            else:
                left = middle + 1
            
        return False