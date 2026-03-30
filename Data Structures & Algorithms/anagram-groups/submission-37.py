class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            anagram[tuple(counter)].append(s)
        return list(anagram.values())
