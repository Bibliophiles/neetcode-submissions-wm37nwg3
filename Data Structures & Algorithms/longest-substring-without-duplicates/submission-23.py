class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        unique_character = set()
        left = 0

        # It's a sliding window
        for right in range(len(s)):
            while s[right] in unique_character:
                # Remove the first character in the string
                unique_character.remove(s[left])
                left += 1

            unique_character.add(s[right])
            longest = max(longest, len(unique_character))
        
        return longest