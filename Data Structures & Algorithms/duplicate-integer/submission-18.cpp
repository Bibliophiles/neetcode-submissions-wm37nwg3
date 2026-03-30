class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int>res(nums.begin(),nums.end());
        return res.size() < nums.size();
    }
};
