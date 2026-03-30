class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        # Counter maps the frequency counts for the characters
        # in each string