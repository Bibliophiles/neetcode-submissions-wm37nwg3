class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        unique_char = set()
        left = 0

        for right in range(len(s)):
            while s[right] in unique_char:
                unique_char.remove(s[left])
                left += 1

            unique_char.add(s[right])
            longest = max(len(unique_char), longest)

        return longest

        # Get additional examples to validate the idea or 
        # the algorithm