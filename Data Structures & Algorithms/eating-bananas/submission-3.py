class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right 

        while left <= right:
            k = (left + right) // 2
            total_banana_per_hour = 0
            for pile in piles:
                total_banana_per_hour += math.ceil(float(pile) / k)
            
            if total_banana_per_hour <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res
            