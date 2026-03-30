class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int s = nums.size();
        vector<int> answer(2,0);
        for (int i=0; i < s; i++){
            for(int j=i+1; j < s; j++){
                if(nums[i]+nums[j]==target){
                    answer[0]=i;
                    answer[1]=j;
                    return answer;
                }    
            }                        
        }
        return {};
    }
};
