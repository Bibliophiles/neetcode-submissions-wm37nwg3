class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int>isDuplicate(nums.begin(), nums.end());
        return isDuplicate.size() < nums.size();
    }
};
