class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int>freq;
        for(int& c : nums){
            freq[c]++;
        }
        vector<vector<int>>res(nums.size() + 1);
        for(auto& p : freq){
            res[p.second].push_back(p.first);
        }
        vector<int>result;
        for(int i = res.size() - 1; i > 0; i--){
            for(auto& f : res[i]){
                result.push_back(f);
            }
            if(result.size() == k){
                return result;
            }
        }
        return result;
    }
};
//Question: store the answer in a vector... the pair had integers check that