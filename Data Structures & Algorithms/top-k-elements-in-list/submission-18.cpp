class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>freq; //This will store the n and its frequency
        for(int& c : nums){
            freq[c]++;
        }

        vector<vector<int>>res(nums.size() + 1);
        for(auto& pair : freq){ // we will take each pair from the freq map
            res[pair.second].push_back(pair.first); // we will store the frequencies in the key position and the numbers themselves in the value position
        }

        vector<int>result;
        for(int i = res.size() - 1; i > 0; i--){ //since we want the most frequent elements, we will take the index from the largest we have which is the last and take it from there
            for(auto& c : res[i]){ //we will take the elements in the list of freq at the biggest index and add it's values to the result
                result.push_back(c);
                if(result.size() == k){
                    return result;
                }
            }
        }
        return result;

    }
};
