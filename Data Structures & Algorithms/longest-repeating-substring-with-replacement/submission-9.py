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
            char_count[s[right]] += 1
            most_frequent = max(most_frequent, char_count[s[right]])
            while right - left + 1 - most_frequent > k:
                char_count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest