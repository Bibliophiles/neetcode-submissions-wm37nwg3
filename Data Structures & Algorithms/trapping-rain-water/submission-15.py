class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_boundary, right_boundary = height[left], height[right]
        trapped_water = 0

        while left < right:
            if left_boundary < right_boundary:
                left += 1
                left_boundary = max(left_boundary, height[left])
                trapped_water += left_boundary - height[left]
            else:
                right -= 1
                right_boundary = max(right_boundary, height[right])
                trapped_water += right_boundary - height[right]

        return trapped_water