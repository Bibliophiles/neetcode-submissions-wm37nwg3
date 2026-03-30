class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>diffToIndex;
        for(int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            if(diffToIndex.find(diff) != diffToIndex.end()){
                return {diffToIndex[diff], i};
            }
            diffToIndex.insert({nums[i], i});
        }
        return {};

    }
};
