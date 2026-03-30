class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
    int s = nums.size();
     for(int i = 0; i < s; ++i){
        for(int j = 0; j < s; ++j){
            if(i != j){
                if(nums[i] == nums[j]){
                    return true;
                }
            }
        }
     }
     return false;
    }
};
