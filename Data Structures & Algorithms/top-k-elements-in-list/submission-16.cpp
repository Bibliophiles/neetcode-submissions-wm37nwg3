class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>numToFrequency;
        for(int& n : nums){
            numToFrequency[n]++;
        }
       vector<vector<int>>temp(nums.size() + 1);
       for(auto& pair : numToFrequency){
            temp[pair.second].push_back(pair.first);
       }
       vector<int>result;
       for(int i = temp.size() - 1; i >= 0; i--){
            for(auto& n : temp[i]){
                result.push_back(n);
                if(result.size() == k){
                    return result;
                }
            }
       }
       return result;

    }
};
