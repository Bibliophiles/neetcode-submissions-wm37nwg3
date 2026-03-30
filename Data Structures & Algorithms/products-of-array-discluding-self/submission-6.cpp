class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int>result(nums.size(), 1);
        for(int i = 1; i < nums.size(); i++){
            result[i] = result[i - 1] * nums[i - 1];
        }
        int postfix = 1;
        for(int i = nums.size() - 1; i >= 0; i--){
            result[i] *= postfix;
            postfix *= nums[i]; //if we started the postfix from 1, why do we need the last value in the nums array
        }
        return result;
    }
};

//the first postfix will always be zero
//the next postfix is the product of the first postfix and the next value in the 
//nums array at i. it's a product that is why we are multiplying
//the result[i] already contains 1, so when multiply the postfix, we will get the same result
//without any issues
//we start i from the last value in the postfix, because we just want to multiply it with 1
