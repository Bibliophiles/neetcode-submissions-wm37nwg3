class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>res;
        for(auto& s : strs){
            string ori = s;
            vector<int>count(26,0);
            for(char& c : ori){
                count[c - 'a']++;
            }
            string key = to_string(count[0]);
            for(int i = 1; i < 25 ; i++){
                key += "," + to_string(count[i]);
            }
            res[key].push_back(s);
        }
        vector<vector<string>>result;
        for(auto& n : res){
            result.push_back(n.second);
        }
        return result;
    }
};
