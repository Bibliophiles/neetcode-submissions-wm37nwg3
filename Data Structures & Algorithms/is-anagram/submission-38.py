class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # You would have easily sorted them and compare
        
        # Solution 1
        # return sorted(s) == sorted(t)
        
        # Count the frequency of each character using the counter
        # frequency map and compare if they are equal

        # Solution 2
        #return Counter(s) == Counter(t)

        #But we need an optimal solution 
        # We will store the count of each character in a count
        # And decrease and increase if a character is found
        # The final counter should have zeros if it's an anagram
        # You then return True or False based on this

        # We will first check the length of the strings 
        # And return False immediately if they are not equal

        if len(s) != len(t):
            return False

        counter = [0] * 26 # Since there are a fixed number of characters 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1 # We cancel 
            #if the two characters are present in both strings
        # Since this is for one string, we don't need to 
        # recreate the counter for each flow of string
        # counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] increase for a and afterward decrease it back to 0 with t

        # Checking if the two strings are anagrams
        for val in counter:
            if val != 0:
                return False   
        
        # After running through the loop with no anti-zeros
        # we can return true
        return True

