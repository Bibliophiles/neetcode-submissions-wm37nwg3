class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
       unordered_map<int , int> count;
       for(auto& val : nums){
        count[val]++;
       }
       vector<pair<int, int>>freqR;
       for(auto& p : count){
        freqR.push_back({p.second, p.first});
       }
       sort(freqR.rbegin(), freqR.rend());
       vector<int>result;
       for(int i = 0; i < k; i++){
        result.push_back(freqR[i].second);
       }
       return result;
    }
};