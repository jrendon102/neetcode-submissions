class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        stash = [0] * 27
        for c in s:
            stash[ord(c) - 96] += 1

        for c in t:
            if not stash[ord(c) - 96]:
                return False
            stash[ord(c) - 96] -= 1
        return True