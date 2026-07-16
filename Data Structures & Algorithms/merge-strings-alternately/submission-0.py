class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        s = ""
        while True:
            if p1 >= len(word1) and p2 >= len(word2):
                return s
            if p1 < len(word1):
                s += word1[p1]
                p1 += 1
            if p2 < len(word2):
                s += word2[p2]
                p2 += 1
            
            
