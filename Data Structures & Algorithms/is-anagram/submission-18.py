class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # let's first define what an anagram is: 
        # an anagram is a string that contains the exact same characters
        # as another string, but the order of the characters can be different.

        
        # one solution is, we can store all the values in a dictionary, 
        # and say if they have the same length, then we can proceed

        if len(s) != len(t):
            return False

        # we want to iterate over one string: acting as the main string
        # and the other acts as the template for comparison 
        # one best way, would have been to sort the values and straight forward compare
        # but that would take log memory

        # Sort both s and t
        #s_sorted = sorted(s)
        #t_sorted = sorted(t)

        #return True if sorted(t) == sorted(s) else False

        # DIFFERENT APPROACH 

        # Take one string as the main and the other as a template for comparison
        # we want to create a dictionary to store the character it's ascii number

        count_s = Counter(s)
        count_t = Counter(t)

        return count_s == count_t
    
    # The idea was to count the number of characters in the string 
    # after making sure they are equal in lenght





