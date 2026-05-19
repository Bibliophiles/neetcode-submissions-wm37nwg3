class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length, s2_length = len(s1), len(s2)

        if s1_length > s2_length:
            return False 
        
        s1_char_count = [0] * 26
        s2_char_count = [0] * 26

        for right in range(len(s1)):
            s1_char_count[ord(s1[right]) - ord('a')] += 1
            s2_char_count[ord(s2[right]) - ord('a')] += 1

        if s1_char_count == s2_char_count:
            return True
        
        for right in range(s1_length, s2_length):
            incoming_character = s2[right]
            outgoing_character = s2[right - s1_length]

            s2_char_count[ord(incoming_character) - ord('a')] += 1
            s2_char_count[ord(outgoing_character) - ord('a')] -= 1

            if s1_char_count == s2_char_count:
                return True
        
        return False