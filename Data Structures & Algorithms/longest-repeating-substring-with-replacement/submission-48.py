class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_window = 0
        most_frequent = 0
        left = 0
        char_count = defaultdict(int)

        for right in range(len(s)):
            char_count[s[right]] += 1
            most_frequent = max(most_frequent, char_count[s[right]])

            while right - left + 1 > most_frequent + k:
                char_count[s[left]] -= 1
                left += 1

            longest_window = max(longest_window, right - left + 1)
        
        return longest_window