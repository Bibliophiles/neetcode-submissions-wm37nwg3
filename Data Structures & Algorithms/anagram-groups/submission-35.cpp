class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>keyToAnagrams;
        for(auto& s : strs){
            vector<int>charCount(26,0);
            for(auto& c : s){
                charCount[c - 'a']++;
            }
            string key = to_string(charCount[0]);
            for(int i = 1; i < 26; i++){
                key += ',' + to_string(charCount[i]);
            }
            keyToAnagrams[key].push_back(s);
        }
        vector<vector<string>>result;
        for(auto& ana : keyToAnagrams){
            result.push_back(ana.second);
        }
        return result;
    }
};
