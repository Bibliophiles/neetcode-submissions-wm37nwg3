class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # You would have easily sorted them and compare
        # Solution 1
        return sorted(s) == sorted(t)