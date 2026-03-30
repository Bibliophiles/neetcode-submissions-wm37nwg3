class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        start_index = 0
        result = []
        while start_index < len(s):
            pound_index = start_index
            # Find the pound - anything before it is the len of the string
            while s[pound_index] != '#': # pound entered as zero
                pound_index += 1 # Found the pound symbol
            # Get the length of the string
            str_length = int(s[start_index : pound_index]) # 10 here 10#Hello
            start_index = pound_index + 1 # We want to include H
            string_en = s[start_index : start_index + str_length]
            result.append(string_en)
            start_index += str_length # it will start on the first character of the next string
        return result
