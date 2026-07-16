class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_count, t_count = {}, {}

        for c in range(len(s)):
            s_count[s[c]] = s_count.get(s[c], 0) + 1
            t_count[t[c]] = t_count.get(t[c], 0) + 1

        return s_count == t_count