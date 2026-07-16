class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string s = "";
        for (int c = 0; c < strs[0].size(); c++) {
            char letter = strs[0][c];
            for (int r = 0; r < strs.size(); r++) {
                if (strs[r][c] != letter) {
                    return s;
                }
            }
            s.push_back(letter);
        }
        return s;
    }
};