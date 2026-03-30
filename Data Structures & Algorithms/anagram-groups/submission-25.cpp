class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
       unordered_map<string, vector<string>>sMap;
       for(auto& str : strs){
         string original = "";
         original = str;
         sort(str.begin(), str.end());
         sMap[str].push_back(original);
       }
       
       vector<vector<string>>res;
       for(auto& pair : sMap){
          res.push_back(pair.second);
       }
       return res;

    }
};