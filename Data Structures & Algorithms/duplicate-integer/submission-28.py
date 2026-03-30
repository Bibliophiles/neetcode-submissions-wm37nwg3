class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # the goal is to save the numbers in a hash_set and compare
        # based on the number of elements in the hashset

        # if the elements in the hash_set is less than the number of elements 
        # in the original array set, then it contained duplicates

        # we can use one python liner with a boolean, if len of this hash_set -> len of the array set
        # In this case we used a set because a set stores only unique numbers

        #if len(set(nums)) < len(nums):
        #    return True
        #else:
        #    return False

        return len(set(nums)) < len(nums)