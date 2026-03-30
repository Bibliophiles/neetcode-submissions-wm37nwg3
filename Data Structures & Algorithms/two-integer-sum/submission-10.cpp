class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Map to store numbers and their indices
        unordered_map<int, int> indexMap;

        // Iterate through the array
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i]; // Calculate the required complement

            // Check if the complement exists in the map
            if (indexMap.find(complement) != indexMap.end()) {
                return {indexMap[complement], i}; // Return indices if found
            }

            // Store the current number and its index in the map
            indexMap[nums[i]] = i;
        }

        return {}; // Return an empty vector if no solution is found
    }
};