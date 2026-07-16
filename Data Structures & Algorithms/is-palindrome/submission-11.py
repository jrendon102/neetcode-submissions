class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr = 0
        right_ptr = len(s) - 1

        while left_ptr < right_ptr:
            while left_ptr < right_ptr and not s[left_ptr].isalpha() and not s[left_ptr].isdigit():
                left_ptr += 1
            while left_ptr < right_ptr and not s[right_ptr].isalpha() and not s[right_ptr].isdigit():
                right_ptr -= 1
            if s[left_ptr].lower() != s[right_ptr].lower():
                return False
            else:
                left_ptr += 1
                right_ptr -= 1
        return True



            