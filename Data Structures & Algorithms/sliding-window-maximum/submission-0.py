class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)

        #Edge cases
        if not nums or k < 0 or k > n:
            return []

        cur_win = [nums[right] for right in range(k)]
        res.append(max(cur_win))

        for i in range(k, n):
            cur_win.append(nums[i])
            cur_win.remove(nums[i - k])
            res.append(max(cur_win))

        return res