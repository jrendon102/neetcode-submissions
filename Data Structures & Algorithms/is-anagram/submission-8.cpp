class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        
        std::unordered_map<char, int> sMap;
        std::unordered_map<char, int> tMap;

        for (int c = 0; c < s.length(); c++)
        {
            sMap[s[c]]++;
            tMap[t[c]]++;
        }

        for (int c = 0; c < sMap.size(); c++)
        {
            if (sMap[c] != tMap[c]) return false;
        }
        return true;
    }
};
