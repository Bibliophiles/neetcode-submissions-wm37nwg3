class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate total rainwater trapped between elevation bars.

        Strategy: Two Pointers
        - Track the max height seen from the left and right sides.
        - The shorter side determines how much water can be trapped at that position.
        - Always move the shorter side inward.
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:

            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water_at_left = left_max - height[left]
                total_water += water_at_left

            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_at_right = right_max - height[right]
                total_water += water_at_right

        return total_water