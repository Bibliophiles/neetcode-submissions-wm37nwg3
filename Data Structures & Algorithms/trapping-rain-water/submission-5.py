class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        left, right = 0, len(height) - 1
        left_boundary, right_boundary = height[left], height[right]

        while left < right:

            if left_boundary < right_boundary:
                left += 1
                left_boundary = max(left_boundary, height[left])
                water = left_boundary - height[left]
                trapped += water
            else:
                right -= 1
                right_boundary = max(right_boundary, height[right])
                water = right_boundary - height[right]
                trapped += water

        return trapped