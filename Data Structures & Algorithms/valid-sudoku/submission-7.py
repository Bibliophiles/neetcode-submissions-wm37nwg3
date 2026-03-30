class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_mask = [0] * 9
        row_mask = [0] * 9
        col_mask = [0] * 9

        for row in range(9):
            for col in range(9):

                if board[row][col] == '.':
                    continue
                
                bit_digit = int(board[row][col]) - 1
                digit_mask = 1 << bit_digit
                box_index = (row // 3) * 3 + (col // 3)

                if digit_mask & row_mask[row]:
                    return False
                
                if digit_mask & col_mask[col]:
                    return False

                if digit_mask & box_mask[box_index]:
                    return False

                # Set the mask values
                row_mask[row] |= digit_mask
                col_mask[col] |= digit_mask
                box_mask[box_index] |= digit_mask

        return True