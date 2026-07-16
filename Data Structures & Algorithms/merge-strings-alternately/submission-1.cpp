class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int l = 0;
        int r = 0;
        string str;
        while (l < word1.size() && r < word2.size()) {
            str.push_back(word1[l]);
            str.push_back(word2[r]);
            l++;
            r++;
        }

        for (int i = l; i < word1.size(); i++) {
            str.push_back(word1[i]);
        }

        for (int i = r; i < word2.size(); i++) {
            str.push_back(word2[i]);
        }
        return str;
    }
};