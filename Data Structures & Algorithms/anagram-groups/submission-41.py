class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            group[tuple(count)].append(s)
        return list(group.values())

        # we created a dictionary of lists called group 
        # and created a list with 26 spaces called count initialized to zero
        # we increase the position of each character by one for each string to obtain a code 
        # these codes would be the same for anagrams
        # turn the count into a hashable with the tuple which is key
        # and append the string to the hashable key from the tuple
        # We are appending the string to the list because is already initialized
        # by defaultdict to be empty, we append the string to it
        # now we have a dictionary with keys from the count and a list 
        # with strings from s
        # we return these lists from the dictionary as a list