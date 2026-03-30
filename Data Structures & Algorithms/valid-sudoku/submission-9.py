class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_masks = [0] * 9
        col_masks = [0] * 9
        box_masks = [0] * 9

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                bit_precision = int(board[row][col]) - 1
                digit_mask = 1 << bit_precision
                box_mask = (row // 3) * 3 + (col // 3)
                if digit_mask & row_masks[row]:
                    return False
                if digit_mask & col_masks[col]:
                    return False
                if digit_mask & box_masks[box_mask]:
                    return False 

                row_masks[row] |= digit_mask
                col_masks[col] |= digit_mask
                box_masks[box_mask] |= digit_mask

        return True