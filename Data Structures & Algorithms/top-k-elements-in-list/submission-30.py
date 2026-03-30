class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = defaultdict(list)

        for num in nums:
            count[num] += 1
        # this dictionary will count the number of numbers

        # now let's reverse it
        for num, cnt in count.items():
            freq[cnt].append(num)

        # we want to be able to return a list of the top k elements
        result = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result