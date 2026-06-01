class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        left = 0
        longest_window = 0

        for right in range(len(s)):
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1
            
            unique_chars.add(s[right])
            longest_window = max(longest_window, len(unique_chars))

        return longest_window