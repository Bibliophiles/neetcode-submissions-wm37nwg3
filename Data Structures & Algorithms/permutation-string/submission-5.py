class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        #pure logic on the lengths
        if len(s1) > len(s2):
            return False

        #initial populations 
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        #work on the frequency counts
        for i in range(n1):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
        
        if s1_counts == s2_counts:
            return True
        
        for i in range(n1, n2):
            #move to the next index, using the new i
            s2_counts[ord(s2[i]) - 97] += 1
            #since we're shifting, delete or remove the previous index
            #we are not deleting the previous value but the first value or index
            s2_counts[ord(s2[i - n1]) - 97] -= 1
            if s1_counts == s2_counts:
                return True
        return False


