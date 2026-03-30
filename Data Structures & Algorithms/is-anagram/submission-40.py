class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        x = list(s1)
        for i in s2:
            try:
                x.remove(i)
            except:
                return False
        return True