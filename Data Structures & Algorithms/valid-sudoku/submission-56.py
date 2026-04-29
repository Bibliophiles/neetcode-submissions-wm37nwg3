class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_masks = [0] * 9
        col_masks = [0] * 9
        box_masks = [0] * 9

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == '.':
                    continue 

                bit_position = int(board[row][col]) - 1
                digit_mask = 1 << bit_position
                box_index = (row // 3) * 3 + (col // 3)

                if row_masks[row] & digit_mask:
                    return False 
                if col_masks[col] & digit_mask:
                    return False
                if box_masks[box_index] & digit_mask:
                    return False 

                row_masks[row] |= digit_mask
                col_masks[col] |= digit_mask
                box_masks[box_index] |= digit_mask
        
        return True