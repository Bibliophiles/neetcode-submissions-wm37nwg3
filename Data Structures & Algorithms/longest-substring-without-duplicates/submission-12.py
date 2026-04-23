class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_characters = set()
        left, longest = 0, 0

        for right in range(len(s)):
            while s[right] in unique_characters:
                unique_characters.remove(s[left])
                left += 1

            unique_characters.add(s[right])
            longest = max(longest, len(unique_characters))

        return longest