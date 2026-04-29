class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        character_count = defaultdict(int)
        current_most_frequent = 0
        left = 0

        for right in range(len(s)):
            character_count[s[right]] += 1

            # Track the most frequent character in the current window
            current_most_frequent = max(current_most_frequent, character_count[s[right]])

            # Shrink the window from the left if it becomes invalid
            while (right - left + 1) > current_most_frequent + k:
                character_count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest