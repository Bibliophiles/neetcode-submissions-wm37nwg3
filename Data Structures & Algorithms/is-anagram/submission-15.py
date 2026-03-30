class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charSet = 26 * [0]
        for i in range(len(s)):
            charSet[ord(s[i]) - ord('a')] += 1
            charSet[ord(t[i]) - ord('a')] -= 1
        
        for c in charSet:
            if c != 0:
                return False

        return True