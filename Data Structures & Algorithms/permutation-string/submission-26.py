class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length, s2_length = len(s1), len(s2)

        if s1_length > s2_length:
            return False 
        
        s1_char_count = [0] * 26
        s2_char_count = [0] * 26

        def char_index(s: str) -> int:
            return ord(s) - ord('a')

        for i in range(s1_length):
            s1_char_count[char_index(s1[i])] += 1
            s2_char_count[char_index(s2[i])] += 1

        if s1_char_count == s2_char_count:
            return True

        for right in range(s1_length, s2_length):
            incoming_char = s2[right]
            outgoing_char = s2[right - s1_length]

            s2_char_count[char_index(incoming_char)] += 1
            s2_char_count[char_index(outgoing_char)] -= 1

            if s1_char_count == s2_char_count:
                return True

        return False