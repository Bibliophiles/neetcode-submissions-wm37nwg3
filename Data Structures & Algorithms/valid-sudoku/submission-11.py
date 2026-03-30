class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each index (0-8) holds a bitmask representing which digits
        # have been in that row, column, or 3x3 box.
        # e.g. row_masks[0] tracks digits seen in a row 0

        row_masks = [0] * 9
        col_masks = [0] * 9
        box_masks = [0] * 9

        for row in range(9):
            for col in range(9):

                # Skip empty cels
                if board[row][col] == ".":
                    continue

                # Convert digit to a 0-indexed bit position
                # e.g. "1" -> 0, "5" -> 4, "9" -> 8
                bit_position = int(board[row][col]) - 1

                # Create a mask with only that bit set
                digit_mask = 1 << bit_position

                # Map (row, col) to one of 9 boxes (0-8)
                # Rows 0-2 / Cols 0-2 -> box 0
                # Row 0-2 / Cols 3-5 -> box 1 ... and so on
                box_index = (row // 3) * 3 + (col // 3)

                # -- Duplicate checks --- 
                # If the bit is already set, this digit has been seen before -> invalid
                if digit_mask & row_masks[row]:
                    return False 
                if digit_mask & col_masks[col]:
                    return False 
                if digit_mask & box_masks[box_index]:
                    return False

                # --- Mark digit as seen --- 
                # Set the bit in the appropriate row, column, and box mask
                row_masks[row] |= digit_mask
                col_masks[col] |= digit_mask
                box_masks[box_index] |= digit_mask

        # All cells passed validation 
        return True