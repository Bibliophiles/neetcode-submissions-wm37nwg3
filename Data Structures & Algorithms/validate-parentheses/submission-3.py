class Solution:
    def isValid(self, s: str) -> bool:
        # Check for the len of the string to be even
        if len(s) % 2 != 0:
            return False
        # to map the closing brackets to the open brackets
        hashmap = {')':'(', '}':'{', ']':'['}
        # a stack to store the open brackets
        stack = []
        # iterate through the s string 
        for c in s:
            # check if c is a closing string
            if c in hashmap:
                # check if stack is not empty and has corresponding mapping
                if stack and stack[-1] == hashmap[c]:
                    # pop the corresponding open bracket from the stack
                    stack.pop()
                else:
                    # If mapping do not match
                    return False
            else:
                # Append the character - open bracket to the stack
                stack.append(c)
        
        # Check that stack is empty to be valid else False
        return True if not stack else False