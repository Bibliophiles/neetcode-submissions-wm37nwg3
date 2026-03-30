class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int>freqCount;
        for(int n : nums){
            freqCount[n]++;
        }
        vector<vector<int>>freqPair(nums.size() + 1);
        for(auto& pair : freqCount){
            freqPair[pair.second].push_back(pair.first);
        }
        vector<int>result;
        for(int i = freqPair.size() - 1; i >= 0; i--){
            for(auto& c : freqPair[i]){
                result.push_back(c);
            }
            if(result.size() == k){
                return result;
            }
        }
        return result;
    }
};
