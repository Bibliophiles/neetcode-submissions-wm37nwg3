class Solution:
    def isValid(self, s: str) -> bool:
        # Check the length of the s to be even else return False because of pairs
        if len(s) % 2 != 0:
            return False
        #Create a hashmap to map the closing brackets to the opening brackets
        hashmap = {')':'(', ']':'[', '}':'{'}
        # Create a stack to store the open open brackets/ and for popping as well
        stack = []
        # Iterate through each character in the s string
        for c in s:
            # If c is a closing bracket
            if c in hashmap:
                # Check if the stack is not empty and the closing bracket maps to an opening bracket in the stack
                if stack and stack[-1] == hashmap[c]:
                    # If it does, remove the last opening bracket from the stack
                    stack.pop()
                else: # Else, they do not match
                    return False
            else: # c is an opening bracket
                # append c to the stack
                stack.append(c)

        return True if not stack else False



# I think the logic of this question comes from studying the question itself
# and how the flow goes
# You must start with an open bracket, right after the opening bracket, the next closing bracket must be of the same type
# And the stack must not be empty