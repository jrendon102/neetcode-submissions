class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        stash = {}
        for c in s:
            if stash.get(c, 0):
                stash[c] += 1
            else:
                stash[c] = 1
        
        for c in t:
            if not stash.get(c):
                return False
            stash[c] -= 1
        
        return True            
                