class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for key, value in count.items():
            freq[value].append(key)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if k == len(result):
                    return result
