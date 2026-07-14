class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        int arr[27] = {};
        int position;
        for (int i = 0; i < s.size(); i++) {
            position = s[i] - 'a' + 1;
            arr[position] += 1;
        }

        for (int i = 0; i < t.size(); i++) {
            position = t[i] - 'a' + 1;
            if (!arr[position]) {
                return false;
            }
            arr[position] -= 1;
        }
        return true;
    }
};
