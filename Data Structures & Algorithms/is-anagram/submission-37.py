class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # You would have easily sorted them and compare
        
        # Solution 1
        # return sorted(s) == sorted(t)
        
        # Count the frequency of each character using the counter
        # frequency map and compare if they are equal
        # Solution 2
        return Counter(s) == Counter(t)

