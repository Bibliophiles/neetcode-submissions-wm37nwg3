class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) - 1
        left = 0
        
        while left <= n:
            if target <= matrix[left][-1]:
                if target in matrix[left]:
                    return True
            left += 1

        return False