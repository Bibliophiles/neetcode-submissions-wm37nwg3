class Solution {
public:

    string encode(vector<string>& strs) {
        string s;
        for(auto& w : strs){
            s += to_string(w.size()) + "#" + w; //2#me
        }
        return s;
    }

    vector<string> decode(string s) {
        vector<string>result;
        int i = 0;
        while(i < s.size()){

            int j = i; //you want to start find the delimiter from the beginning of the string

            while(s[j] != '#'){
                 j++; //position of delimiter
            }

            int length = stoi(s.substr(i, j - i));
            i = j + 1;
            string w = s.substr(i, length);
            result.push_back(w);
            i = i + length;
        }

        return result;
    }
};
