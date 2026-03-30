class Solution {
public:

    string encode(vector<string>& strs) {
        string s;
        for(auto& w : strs){
            s += to_string(w.size()) + "#" + w;
        }
        return s;
    }

    vector<string> decode(string s) {
        vector<string>result;
        int i = 0;
        while(i < s.size()){
            int j = i;
            while(s[j] != '#'){ //find the delimiter
                j++;
            }
            int length = stoi(s.substr(i, j - i)); //get a value say 2 from 2#me
            i = j + 1; //move i from 2 to m, since j is the delimiter #
            result.push_back(s.substr(i, length)); //the length 2 for me
            i = j+1+length; //move i to the end of the string
        }
        return result;
    }
};
