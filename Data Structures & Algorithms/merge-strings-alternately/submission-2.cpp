class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int ptr1 = 0;
        int ptr2 = 0;
        string s = "";
        while (true) {
            if (ptr1 >= word1.size() && ptr2 >= word2.size()) {
                return s;
            }
            if (ptr1 < word1.size()) {
                s += word1[ptr1++];
            }
            if (ptr2 < word2.size()) {
                s += word2[ptr2++];
            }
        }
        return s;
    }
};