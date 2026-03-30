class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>freq;
        for(auto& c : nums){
            freq[c]++;
        }
        vector<vector<int>>indexFreq(nums.size() + 1);
        for(auto& pair : freq){
            indexFreq[pair.second].push_back(pair.first);
        }
        vector<int>result;
        for(int i = indexFreq.size() - 1; i >= 0; i--){
            for(auto& c : indexFreq[i]){
                result.push_back(c);
            }
            if(result.size() == k){
                return result;
            }
        }
        return result;
    }
};
