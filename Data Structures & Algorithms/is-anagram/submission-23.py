class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # You want to return the count of each character in the string
        # If both the length and frequency count is the same; it's an anagram

        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)