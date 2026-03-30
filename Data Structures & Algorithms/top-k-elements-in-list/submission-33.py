class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = defaultdict(list) # numbers with the same frequencies can share each other with the same key
        # they would be grouped based on their frequencies 

        for num in nums:
            count[num] += 1 # will store the number and it's counts
        # One occurred 3 times -- the first counter won't be the most organized
        # Two also occurred 3 times 
        # So we store 3 - and give it One and Two in a list

        #invert the number and the count 
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Now we want the number that occurred the most 
        # That would be the numbers with the highest frequencies
        # And this would boil downwards
        # We can use a for loop that begins from the length of the array
        # And bubbles downwards, since we know no number can occurred more than the length of the array

        result = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]: # freq[i] contains the list of the numbers, we loop over it
                result.append(num)
                # we only want the k most frequent elements so we want k size result
                if len(result) == k:
                    return result