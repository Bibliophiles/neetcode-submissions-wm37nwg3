class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>groupedAnagrams;
        for(const auto& element : strs){
            vector<int>charCount(26,0); 
            for(char character : element){
                charCount[character - 'a']++;
            }
            string key = to_string(charCount[0]);
            for(int i = 1; i < 26; i++){
                key += ',' + to_string(charCount[i]); 
            }
            groupedAnagrams[key].push_back(element);
        }
        vector<vector<string>>result;
        for(const auto& anagram : groupedAnagrams){
            result.push_back(anagram.second); 
        }
        return result;
    }
};
