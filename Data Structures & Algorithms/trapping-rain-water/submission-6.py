class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height)-1
        left_max , right_max = height[left], height[right]
        while left < right:
            if height[left] < height [right]:
                left += 1
                left_max = max(left_max, height[left])
                water += max(0, left_max - height[left])
            else :
                right -= 1
                right_max = max(right_max, height[right])
                water += max(0, right_max - height[right])
        return water   
        
# Input: height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9