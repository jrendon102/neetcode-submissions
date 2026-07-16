class Solution:
    def isPalindrome(self, s: str) -> bool:
        lptr = 0
        rptr = len(s) - 1

        while lptr < rptr:
            while lptr < rptr and not s[lptr].isalnum():
                lptr += 1
            while rptr > lptr and not s[rptr].isalnum():
                rptr -= 1
            if s[lptr].lower() != s[rptr].lower():
                print(s[lptr])
                print(s[rptr])
                return False
            
            lptr += 1
            rptr -= 1

        return True