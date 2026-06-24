class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        longest, left, most_char = 0, 0, 0

        for right in range(len(s)):
            char_count[s[right]] += 1
            most_char = max(most_char, char_count[s[right]])

            while right - left + 1 - most_char > k:
                char_count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        
        return longest