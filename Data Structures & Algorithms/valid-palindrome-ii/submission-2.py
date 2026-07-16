class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return self.is_pal(s, l + 1, r) or self.is_pal(s, l, r - 1)
            l += 1
            r -= 1
        return True


    def is_pal(self, s, left, right):
        l = left
        r = right
        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
