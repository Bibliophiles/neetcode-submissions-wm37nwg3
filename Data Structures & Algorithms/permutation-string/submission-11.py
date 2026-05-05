class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Check if any permutation of s1 exists as a substring of s2.

        Strategy: Fixed-Size Sliding Window
        - A permutation has the same character counts as the original.
        - Slide a window of size len(s1) across s2.
        - If the character counts match at any point, a permutation exists.
        """
        s1_length, s2_length = len(s1), len(s2)

        if s1_length > s2_length:
            return False

        def char_index(c: str) -> int:
            return ord(c) - ord('a')

        s1_char_counts = [0] * 26
        window_char_counts = [0] * 26

        # Build initial counts for s1 and the first window in s2
        for i in range(s1_length):
            s1_char_counts[char_index(s1[i])] += 1
            window_char_counts[char_index(s2[i])] += 1

        if s1_char_counts == window_char_counts:
            return True

        # Slide the window across s2
        for right in range(s1_length, s2_length):
            incoming_char = s2[right]
            outgoing_char = s2[right - s1_length]

            # Expand window by adding the incoming character
            window_char_counts[char_index(incoming_char)] += 1

            # Shrink window by removing the outgoing character
            window_char_counts[char_index(outgoing_char)] -= 1

            if s1_char_counts == window_char_counts:
                return True

        return False