class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length, s2_length = len(s1), len(s2)

        if s1_length > s2_length:
            return False

        s1_char_counts = [0] * 26
        window_char_counts = [0] * 26

        # Build initial counts for s1 and the first window in s2
        for i in range(s1_length):
            s1_char_counts[ord(s1[i]) - ord('a')] += 1
            window_char_counts[ord(s2[i]) - ord('a')] += 1

        if s1_char_counts == window_char_counts:
            return True

        # Slide the window across s2
        for right in range(s1_length, s2_length):
            incoming_char = s2[right]
            outgoing_char = s2[right - s1_length]

            # Expand window by adding the incoming character
            window_char_counts[ord(incoming_char) - ord('a')] += 1

            # Shrink window by removing the outgoing character
            window_char_counts[ord(outgoing_char) - ord('a')] -= 1

            if s1_char_counts == window_char_counts:
                return True

        return False