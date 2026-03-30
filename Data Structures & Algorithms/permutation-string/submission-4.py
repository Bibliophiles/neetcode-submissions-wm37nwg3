class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer, it can't be a permutation of any substring in s2
        if len(s1) > len(s2):
            return False
        
        # Frequency arrays for 26 lowercase letters
        s1_count = [0] * 26
        s2_count = [0] * 26

        # Populate the initial frequency counts
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # Count how many characters match in frequency
        matches = sum(1 for i in range(26) if s1_count[i] == s2_count[i])

        # Sliding window: move right end of the window one character at a time
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Incoming character at the right end of the window
            index_in = ord(s2[right]) - ord('a')
            s2_count[index_in] += 1
            if s1_count[index_in] == s2_count[index_in]:
                matches += 1
            elif s1_count[index_in] + 1 == s2_count[index_in]:
                matches -= 1

            # Outgoing character at the left end of the window
            index_out = ord(s2[right - len(s1)]) - ord('a')
            s2_count[index_out] -= 1
            if s1_count[index_out] == s2_count[index_out]:
                matches += 1
            elif s1_count[index_out] - 1 == s2_count[index_out]:
                matches -= 1

        # Final check for the last window
        return matches == 26
