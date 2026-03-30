class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Check the length of the list and the length when placed in a set
        # Return True or False based on the length
        return len(set(nums)) < len(nums)