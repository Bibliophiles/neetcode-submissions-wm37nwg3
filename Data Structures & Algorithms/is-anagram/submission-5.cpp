class Solution {
public:
    bool isAnagram(string s, string t) {
        // Anagrams must have the same length
        if (s.length() != t.length()) {
            return false;
        }

        // Array to count character frequencies
        vector<int> charCount(26, 0);

        // Increment for characters in `s` and decrement for `t`
        for (int i = 0; i < s.length(); ++i) {
            charCount[s[i] - 'a']++;
            charCount[t[i] - 'a']--;
        }

        // Check if all counts are zero
        for (int count : charCount) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }
};