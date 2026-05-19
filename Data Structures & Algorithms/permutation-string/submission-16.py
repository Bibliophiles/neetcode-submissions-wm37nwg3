class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length, s2_length = len(s1), len(s2)

        if s1_length > s2_length:
            return False
        
        s1_char_count = [0] * 26
        s2_char_count = [0] * 26

        for i in range(s1_length):
            s1_char_count[ord(s1[i]) - ord('a')] += 1
            s2_char_count[ord(s2[i]) - ord('a')] += 1

        if s1_char_count == s2_char_count:
            return True

        for right in range(s1_length, s2_length):
            incoming_character = s2[right]
            outgoing_character = s2[right - s1_length] #the first character in the s2 must go
            # get the character counts for this window
            s2_char_count[ord(incoming_character) - ord('a')] += 1
            s2_char_count[ord(outgoing_character) - ord('a')] -= 1
            # it's only one character we add in each slide, so we only count for that

            if s1_char_count == s2_char_count:
                return True

        return False 