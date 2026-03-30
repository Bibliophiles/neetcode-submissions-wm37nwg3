class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = defaultdict(list)

        for num in nums:
            count[num] += 1 # 1 : 1
                            # 2 : 3
                            # 3 : 2
                            # 4 : 3

        for num, cnt in count.items():
            freq[cnt].append(num) # 3 : [2, 4]
                                  # 1 : [1]
                                  # 2 : [3]

        result = []
        for i in range(len(nums), 0, -1): # len(nums) i = 3, now decrease
            for num in freq[i]: # [2, 4]
                result.append(num) # 2
                if len(result) == k: # [2, 4]
                    return result