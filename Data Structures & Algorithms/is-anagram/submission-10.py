class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars = dict()
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        
        for char in t:
            if char not in chars or chars[char] == 0:
                return False
            chars[char] -= 1
        return True