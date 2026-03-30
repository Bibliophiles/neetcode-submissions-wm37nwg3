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
            while(s[j] != '#'){
                j++;
            }
            int length = stoi(s.substr(i, j - i));
            i = j + 1;
            result.push_back(s.substr(i, length));
            i += length;
        }
        return result;
    }
};
