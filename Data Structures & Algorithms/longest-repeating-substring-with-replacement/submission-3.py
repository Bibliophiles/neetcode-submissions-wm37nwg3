class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countChar = defaultdict(int)
        l, res = 0, 0

        for r in range(len(s)):
            countChar[s[r]] += 1
            max_count = max(countChar.values())

            while (r - l + 1) - max_count > k:
                countChar[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res