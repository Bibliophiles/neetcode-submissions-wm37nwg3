class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # you have an array of numbers, and given a target, 
        # you want to find a number and it's complement to make the target
        # thing is, we are only dealing with their indices and not the number themselves

        # why do you think we need a dictionary here?
        # we are also working with the indexes of the numbers in the array

       # we are going to create a dictionary called seen
       seen = {}
       # we will go through the nums once, and store each number we see together with it's index in the seen 
       # dictionary we created
       for i, num in enumerate(nums):
            # compute the complement
            complement = target - num
            # if this is the first number, then there is no complement in the seen 
            # dictionary yet
            # if there is an element in the seen dictionary, then we can check if the complement would 
            # a number already seen that was stored there
            if complement in seen:
                # return the index of the complement as stored in the dictionary
                # and i would be the index of the current num
                # we return a list of these
                return [seen[complement], i]
            # we can add this number to the seen dictionary
            seen[num] = i
