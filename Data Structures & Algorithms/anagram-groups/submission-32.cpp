class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>>res;
        for(auto& s : strs){
            vector<int>count(26,0);
            for(char& c : s){
                count[c - 'a']++; //we will count each character each element
            } // store the count in a string
            string key = to_string(count[0]);
            for(int i = 1; i < 26; i++){
                key += "," + to_string(count[i]); //we store the count of each character in the string for each element
            } // we can put in the key and the value and check it against other elements in the map for grouping 
            res[key].push_back(s); //this map will group the anagrams according to their keys stored in the string
        }
        vector<vector<string>>result;
        for(auto& n : res){ //we take the vector of strings from the map and store them in the result
            result.push_back(n.second);
        }
        return result;
    }
};
