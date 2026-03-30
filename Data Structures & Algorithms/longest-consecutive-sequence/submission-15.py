class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set:
                current_len = 1
                while num + current_len in num_set:
                    current_len += 1
                longest = max(current_len, longest)
        return longest