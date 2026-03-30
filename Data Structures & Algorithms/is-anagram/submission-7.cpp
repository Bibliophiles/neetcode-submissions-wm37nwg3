class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }

       vector<int>grace(26,0);
       for(int i = 0; i < s.length(); ++i){
            grace[s[i] - 'a']++;
            grace[t[i] - 'a']--;
       }

     for(int count : grace){
        if(count != 0){
            return false;
        }
     }

     return true;

     
    }
};
