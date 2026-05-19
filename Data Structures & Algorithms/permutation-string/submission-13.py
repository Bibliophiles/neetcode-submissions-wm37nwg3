class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length, s2_length = len(s1), len(s2)

        if s1_length > s2_length:
            return False
        
        # keeping check for character count for each string
        s1_char_count = [0] * 26
        s2_char_count = [0] * 26

        for i in range(s1_length):
            s1_char_count[ord(s1[i]) - ord('a')] += 1
            s2_char_count[ord(s2[i]) - ord('a')] += 1

        if s1_char_count == s2_char_count:
            return True

        for right in range(s1_length, s2_length):
            # because we are sliding, there is an incoming character and an outgoing character
            incoming_character = s2[right]
            outgoing_character = s2[right - s1_length]

            # we need to keep count of these new and old character count in the window
            # it needs to reflect in the window - the actual sliding now happens
            # add and remove inside the window and keep count of the characters
            s2_char_count[ord(incoming_character) - ord('a')] += 1
            s2_char_count[ord(outgoing_character) - ord('a')] -= 1

            # we can check if the character counts are still equal to each other
            if s1_char_count == s2_char_count:
                return True 

        return False 