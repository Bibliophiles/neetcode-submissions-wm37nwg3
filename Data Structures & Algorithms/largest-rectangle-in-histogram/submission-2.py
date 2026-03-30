class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores (height, index)
        max_area = 0
        heights.append(0)  # sentinel to empty the stack at the end

        for i, h in enumerate(heights):
            while stack and stack[-1][0] > h:
                stack_h, stack_i = stack.pop()
                width = i if not stack else i - stack[-1][1] - 1
                max_area = max(max_area, stack_h * width)
            stack.append((h, i))
        
        return max_area