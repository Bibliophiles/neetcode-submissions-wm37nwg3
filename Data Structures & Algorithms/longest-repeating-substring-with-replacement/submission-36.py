class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_window = 0
        left = 0
        character_count = defaultdict(int)
        window_most_frequent = 0

        for right in range(len(s)):
            character_count[s[right]] += 1
            window_most_frequent = max(window_most_frequent, character_count[s[right]])

            while right - left + 1 > window_most_frequent + k:
                character_count[s[left]] -= 1
                left += 1

            longest_window = max(longest_window, right - left + 1)

        return longest_window