class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1] * len(nums)
        prefix = 1 

        for i in range(len(nums)):
            prefix_products[i] = prefix
            prefix *= nums[i]

        postfix = 1 
        for i in range(len(nums) - 1, -1, -1):
            prefix_products[i] *= postfix # now becomes prefix * postfix
            postfix *= nums[i]

        return prefix_products