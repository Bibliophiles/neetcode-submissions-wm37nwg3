class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += str(len(s)) + '#' + s
        return st

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        #running through the entire string of strings
        while i < len(s):
            #locating the delimiter
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = 1 + j
            j = i + length
            result.append(s[i:j])
            i = j

        return result
