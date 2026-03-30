class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            # we reinitialized this each time we take a new string
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                # we generate the count for the string
            # we store it and it's associated string in the dictionary
            # but first convert the count from a list to a tuple to make hashable
            group[tuple(count)].append(s)
        
        # return all the values which are the lists in the dictionary
        # return them inside another list
        return list(group.values())