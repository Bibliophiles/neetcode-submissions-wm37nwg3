class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        counts = {}  # Store character counts in the current window

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)  # Increment count of current char

            max_count = max(counts.values())  # Find the most frequent char in the window

            # Check if the current window is valid (can be made all same char with <= k replacements)
            while (r - l + 1) - max_count > k:  # If # of other chars > k, shrink window
                counts[s[l]] -= 1  # Decrement count of char leaving the window
                l += 1  # Shrink the window from the left

            res = max(res, r - l + 1)  # Update the maximum length

        return res