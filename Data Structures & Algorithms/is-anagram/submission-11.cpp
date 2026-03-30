class Solution {
public:
    bool isAnagram(string s, string t) {
        //first, we will check the sizes of the two strings before anything else
        //we will create a charCount to key track of each character for each string
        // the charCount will cancel out for each string simultaneously
        //if its a valid anagram, charCount will contain zeros for each index

        if(s.size() != t.size()){
            return false; //automatically return false if the sizes are not equal
        }

        vector<int>charCount(26,0);
        for(int i = 0; i < s.size(); i++){
            charCount[s[i] - 'a']++; //charCount[25]++ for z
            charCount[t[i] - 'a']--;
        }
        //increase and decrease for each character count

        for(auto& count : charCount){
            if(count != 0){ //go through each index of the charCount and check if it's equal to zero after 
                return false; //after the end of the loop
            } //remember we are dealing with two strings
        }  
        return true; //charCount[_0_0_0_0_0_0_0_0_0_0_0_0_]



    }
};
