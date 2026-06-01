class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}

        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in two_sum:
                return [two_sum[complement], i]
            two_sum[num] = i

        return []