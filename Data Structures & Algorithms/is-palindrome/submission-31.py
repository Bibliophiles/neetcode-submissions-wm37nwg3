class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # skip characters that are not alphanumeric from the left
            while left < right and not s[left].isalnum():
                left += 1
            # skip characters that are not alphanumeric from the right 
            while left < right and not s[right].isalnum():
                right -= 1

            # Check for same character using .lower()
            if s[left].lower() != s[right].lower():
                return False 
            
            # Increment the value of left and right
            left += 1
            right -= 1

        # return True if all conditions are met as a palindrome
        return True