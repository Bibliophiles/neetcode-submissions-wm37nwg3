class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Strategy: Sliding Window
        - right pointer expands the window by adding new characters.
        - left pointer shrinks the window when a duplicate is found.
        - A set tracks all unique characters currently in the window.
        """
        unique_chars = set()
        left = 0
        longest = 0

        for right in range(len(s)):

            # Shrink the window from the left until the duplicate is removed
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1

            # Expand the window by adding the new character
            unique_chars.add(s[right])
            longest = max(longest, len(unique_chars))

        return longest