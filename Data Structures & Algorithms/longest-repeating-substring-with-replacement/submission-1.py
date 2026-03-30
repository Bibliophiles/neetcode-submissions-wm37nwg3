class Solution:
    def characterReplacement(self, s: str, k: int):
        l, res = 0, 0
        counts = defaultdict(int)  # Use defaultdict(int)

        for r in range(len(s)):
            counts[s[r]] += 1  # No need for .get() anymore

            max_count = max(counts.values())

            while (r - l + 1) - max_count > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res