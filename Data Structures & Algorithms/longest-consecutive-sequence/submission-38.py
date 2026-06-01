class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        nums_set = set(nums)

        for num in nums_set:
            if (num - 1) not in nums_set:
                current_length = 1
                while num + current_length in nums_set:
                    current_length += 1
                longest_sequence = max(longest_sequence, current_length)
        
        return longest_sequence