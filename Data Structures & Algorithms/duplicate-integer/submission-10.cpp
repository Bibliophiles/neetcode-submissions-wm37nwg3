using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int s = nums.size();

        for(int i = 0; i < s; i++){
            if (nums[i] == nums[i+1])
                return true;
        }
        return false;
    }
};