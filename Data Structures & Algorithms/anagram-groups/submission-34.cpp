class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>anagramMap;
        for(auto& s : strs){
            vector<int>charCount(26,0);
            for(char& c : s){
                charCount[c - 'a']++;
            }
            string key = to_string(charCount[0]);
            for(int i = 1; i < 26; i++){
                key += "," + to_string(charCount[i]);
            }
            anagramMap[key].push_back(s);
        }
        vector<vector<string>>result;
        for(auto& res : anagramMap){
            result.push_back(res.second);
        }
        return result;
    }
};
