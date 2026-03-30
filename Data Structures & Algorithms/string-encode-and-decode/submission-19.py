class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str
    def decode(self, s: str) -> List[str]:
        result = []
        start_index = 0
        while start_index < len(s):
            pound_index = start_index
            while s[pound_index] != '#':
                pound_index += 1
            str_length = int(s[start_index : pound_index])
            start_index = pound_index + 1
            string_en = s[start_index : start_index + str_length]
            result.append(string_en)
            start_index += str_length
        return result
