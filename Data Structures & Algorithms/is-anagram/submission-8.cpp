class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }

        vector<int>charCount(26,0);
        for(int i = 0; i < s.length(); i++){
            charCount[s[i] - 'a']++;
            charCount[t[i] - 'a']--;
        }

        for(int c : charCount){
            if(c != 0){
                return false;
            }
        }
        return true;

    }
};
