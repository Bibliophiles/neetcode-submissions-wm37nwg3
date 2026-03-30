class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>>res;
        for(auto& str : strs){
            string original = str;
            sort(str.begin(), str.end());
            res[str].push_back(original);
        }
        vector<vector<string>>result;
        for(auto& pair : res){
            result.push_back(pair.second);
        }
        return result;
    }
};
