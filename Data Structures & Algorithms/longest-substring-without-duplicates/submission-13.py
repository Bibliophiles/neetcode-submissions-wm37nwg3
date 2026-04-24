class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        unique_characters = set()
        left = 0

        for right in range(len(s)):
            while s[right] in unique_characters:
                unique_characters.remove(s[left])
                left += 1

            unique_characters.add(s[right])
            longest = max(longest, len(unique_characters))

        return longest