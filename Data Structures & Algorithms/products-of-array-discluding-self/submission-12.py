class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        # res = [1, 1, 1, 1, 1]

        prefix = 1
        for i in range(len(nums)): # nums = [1, 2, 4, 6]
            res[i] = prefix      # res = [prefix, 1, 1, 1, 1]
            prefix *= nums[i]    # res = [prefix, 2] 2 becomes the new prefix
                                 # res = [prefix, prefix, 8]
                                 # res = [prefix, prefix, prefix, 48] prefix now holds 48

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        

            
