class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Find the maximum element in every sliding window of size k.

        Strategy: Monotonic Deque
        - The deque stores indices in decreasing order of their values.
        - The front of the deque is always the index of the current maximum.
        - Remove elements from the back that are smaller than the incoming element.
        - Remove elements from the front that have fallen outside the window.
        """
        output = []
        decreasing_deque = deque()  # stores indices, values decrease front to back
        left = right = 0

        while right < len(nums):

            # Remove from back — smaller elements can never be the maximum
            while decreasing_deque and nums[decreasing_deque[-1]] < nums[right]:
                decreasing_deque.pop()
            decreasing_deque.append(right)

            # Remove from front — index has fallen outside the window
            if left > decreasing_deque[0]:
                decreasing_deque.popleft()

            # Window is fully formed — record the maximum
            if (right + 1) >= k:
                output.append(nums[decreasing_deque[0]])
                left += 1

            right += 1

        return output