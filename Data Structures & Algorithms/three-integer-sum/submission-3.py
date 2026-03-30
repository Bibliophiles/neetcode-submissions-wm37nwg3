class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in nums that sum to zero.

        Strategy: Sort + Two Pointers
        - Fix one number (pivot), then use two pointers to find the complementary pair.
        - Skip duplicates at each position to ensure unique triplets only.
        """
        triplets = []
        nums.sort()

        for pivot_idx, pivot in enumerate(nums):

            # Since the array is sorted, no triplet starting here can sum to 0
            if pivot > 0:
                break

            # Skip duplicate pivots to avoid repeated triplets
            is_duplicate_pivot = pivot_idx > 0 and pivot == nums[pivot_idx - 1]
            if is_duplicate_pivot:
                continue

            # Two-pointer search for pairs that sum to -pivot
            left, right = pivot_idx + 1, len(nums) - 1

            while left < right:
                current_sum = pivot + nums[left] + nums[right]

                if current_sum > 0:
                    right -= 1          # Sum too large → shrink from the right
                elif current_sum < 0:
                    left += 1           # Sum too small → grow from the left
                else:
                    triplets.append([pivot, nums[left], nums[right]])

                    # Advance both pointers inward
                    left += 1
                    right -= 1

                    # Skip duplicates on BOTH sides
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return triplets