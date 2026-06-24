class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counter = defaultdict(int)
        most_char = 0
        longest = 0
        left = 0

        for right in range(len(s)):
            char_counter[s[right]] += 1
            most_char = max(most_char, char_counter[s[right]])

            while right - left + 1 - most_char > k:
                char_counter[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        
        return longest