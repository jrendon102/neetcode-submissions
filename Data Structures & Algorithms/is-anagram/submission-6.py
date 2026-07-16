class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        
        s_map, t_map = {}, {}
        
        for c in range(len(s)):
            s_map[s[c]] = s_map.get(s[c], 0) + 1
            t_map[t[c]] = t_map.get(t[c], 0) + 1
        return s_map == t_map

        return True