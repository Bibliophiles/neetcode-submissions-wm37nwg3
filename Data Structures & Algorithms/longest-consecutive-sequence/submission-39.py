class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        num_set = set(nums)

        for num in num_set:
            if (num - 1) not in num_set:
                current_len = 1
                while num + current_len in num_set:
                    current_len += 1
                longest_seq = max(longest_seq, current_len)

        return longest_seq
