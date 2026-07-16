class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, int> map;
        for (int i=0; i<s.size(); i++) {
            if (map.find(s[i]) != map.end()) {
                map[s[i]] += 1;
            }
            else {
                map[s[i]] = 1;
            }
        }

        for (int i=0; i<t.size(); i++) {
            if (map.find(t[i]) == map.end() || map[t[i]] == 0) {
                return false;
            }
            map[t[i]] -= 1;
        }
        return true;
    }
};
