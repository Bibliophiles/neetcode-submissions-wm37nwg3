class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check for the size of the string
        if len(s) != len(t):
            return False

        #character count for each character in the string
        charCount = [0] * 26
        for c in range(len(s)):
            charCount[ord(s[c]) - ord('a')] += 1
            charCount[ord(t[c]) - ord('a')] -= 1

        #check for zeros
        for w in charCount:
            if w != 0:
                return False

        return True