class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        left = 0
        most_frequent = 0
        longest = 0

        for right in range(len(s)):

            # Expand the window by adding the new character
            char_count[s[right]] += 1

            # Track the most frequent character in the current window
            most_frequent = max(most_frequent, char_count[s[right]])

            # Shrink the window from the left if it becomes invalid
            while right - left + 1 - most_frequent > k:
                char_count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest