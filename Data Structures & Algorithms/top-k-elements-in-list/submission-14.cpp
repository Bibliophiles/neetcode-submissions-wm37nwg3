class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Step 1: Count frequencies of each number
        unordered_map<int, int> numToFrequency;
        for (int num : nums) {
            numToFrequency[num]++;
        }

        // Step 2: Group numbers by their frequencies
        vector<vector<int>> frequencyBuckets(nums.size() + 1);
        for (const auto& [num, freq] : numToFrequency) {
            frequencyBuckets[freq].push_back(num);
        }

        // Step 3: Collect the top k frequent elements
        vector<int> result;
        for (int freq = frequencyBuckets.size() - 1; freq > 0; --freq) {
            for (int num : frequencyBuckets[freq]) {
                result.push_back(num);
                if (result.size() == k) {
                    return result; // Early return once we have k elements
                }
            }
        }

        return result; // Return result (redundant, as we return earlier)
    }
};