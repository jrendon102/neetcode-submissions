class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = ""; 
        for (int c = 0; c < strs[0].size(); c++) {
            char ch = strs[0][c];
            for (int r = 1; r < strs.size(); r++) {
                if (ch != strs[r][c]) {
                    return res;
                }
            }
            res += ch;
        }
        return res;
    }
};