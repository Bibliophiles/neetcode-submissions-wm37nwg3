class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Maps each number to the length of the consecutive sequence it belongs to.
        # defaultdict(int) means any key not yet in the map defaults to 0.
        sequence_length = defaultdict(int)

        longest = 0

        for num in nums:

            # Only process num if we haven't seen it before (avoid duplicate processing)
            if not sequence_length[num]:

                # Check if there is an existing sequence to the left (num - 1)
                # and an existing sequence to the right (num + 1).
                # If they don't exist, defaultdict returns 0, so this still works.
                left_length  = sequence_length[num - 1]
                right_length = sequence_length[num + 1]

                # The total length of the merged sequence is:
                # left sequence + current number + right sequence
                total_length = left_length + 1 + right_length

                # Mark the current number with the total sequence length
                sequence_length[num] = total_length

                # Update the leftmost boundary of the sequence with the total length.
                # This is num minus however far the left sequence stretches.
                sequence_length[num - left_length] = total_length

                # Update the rightmost boundary of the sequence with the total length.
                # This is num plus however far the right sequence stretches.
                sequence_length[num + right_length] = total_length

                # Track the longest sequence found so far
                longest = max(longest, total_length)

        return longest
    