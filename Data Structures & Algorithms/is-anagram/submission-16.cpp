class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char, int> stash;
        for (int i = 0; i < s.size(); i++) {
            if (stash[s[i]]) {
                stash[s[i]] += 1;
            }
            else {
                stash[s[i]] = 1;
            }
        }

        for (int i = 0; i < t.size(); i++) {
            if (stash[t[i]] == 0) {
                return false;
            }
            stash[t[i]] -= 1;
        }
        return true;
    }
};
