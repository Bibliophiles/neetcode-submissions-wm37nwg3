class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find the longest substring where you can replace at most k characters
        to make all characters the same.

        Strategy: Sliding Window
        - right pointer expands the window by adding new characters.
        - left pointer shrinks the window when it becomes invalid.
        - A window is valid when: window_size - most_frequent_char <= k
          (meaning we only need k replacements to make all chars the same)
        """
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
            window_size = right - left + 1
            replacements_needed = window_size - most_frequent
            while replacements_needed > k:
                char_count[s[left]] -= 1
                left += 1
                window_size = right - left + 1
                replacements_needed = window_size - most_frequent

            longest = max(longest, right - left + 1)

        return longest