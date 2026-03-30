class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Find the container that holds the most water.

        Strategy: Two Pointers
        - Start from both ends and work inward.
        - Always move the shorter side, since keeping it can never improve the area.
        """
        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right:
            width = right - left
            current_water = min(heights[left], heights[right]) * width
            max_water = max(max_water, current_water)

            # Move the shorter side inward — keeping it can only shrink the area
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_water