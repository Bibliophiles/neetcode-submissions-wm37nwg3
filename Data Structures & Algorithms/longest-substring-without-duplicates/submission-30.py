class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left, longest = 0, 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            longest = max(longest, len(char_set))

        return longest