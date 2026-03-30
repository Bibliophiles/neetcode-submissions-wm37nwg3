class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Step 1: Count the frequency of each number
        unordered_map<int, int> frequencyMap;
        for (int num : nums) {
            frequencyMap[num]++;
        }

        // Step 2: Group numbers by their frequency
        vector<vector<int>> buckets(nums.size() + 1); // Bucket index = frequency
        for (const auto& entry : frequencyMap) {
            int number = entry.first;
            int frequency = entry.second;
            buckets[frequency].push_back(number);
        }

        // Step 3: Collect the top k frequent elements
        vector<int> result;
        for (int i = buckets.size() - 1; i > 0 && result.size() < k; --i) {
            for (int num : buckets[i]) {
                result.push_back(num);
                if (result.size() == k) {
                    return result; // Return once we have k elements
                }
            }
        }

        return result; // Return the result (handles edge cases)
    }
};