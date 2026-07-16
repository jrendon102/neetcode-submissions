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
        
        chars2 = dict()
        for char in t:
            if char in chars2:
                chars2[char] += 1
            else:
                chars2[char] = 1
        return chars == chars2