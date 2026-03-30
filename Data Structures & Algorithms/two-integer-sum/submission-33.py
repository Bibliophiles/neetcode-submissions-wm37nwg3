class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # you have an array of numbers, and given a target, 
        # you want to find a number and it's complement to make the target
        # thing is, we are only dealing with their indices and not the number themselves

        # why do you think we need a dictionary here?
        # we are also working with the indexes of the numbers in the array

        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            # we created a dictionary that would store the numbers that we passed 
            # together with their index 
            # so we can use the dictionary as a lookup. the nums is all we have for now

            if complement in seen:
                return [seen[complement], i]
            
            # if the complement value is not in the seen dictionary already
            # put the number and it's index inside the dictionary as already seeen values
            seen[num] = i