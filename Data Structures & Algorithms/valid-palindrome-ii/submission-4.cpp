class Solution {
public:
    bool validPalindrome(string s) {
        int leftPtr = 0;
        int rightPtr = s.size() - 1;
        while (leftPtr <= rightPtr) {
            if (s[leftPtr] != s[rightPtr]) {
                return isPal(s, leftPtr + 1, rightPtr) || isPal(s, leftPtr,rightPtr - 1);
            }
            leftPtr++;
            rightPtr--;
        }
        return true;
    }
private:
    bool isPal(string& s, int leftPtr, int rightPtr) {
        while (leftPtr <= rightPtr) {
            if (s[leftPtr] != s[rightPtr]) {
                return false;
            }
            leftPtr++;
            rightPtr--;
        }
        return true;
    }
};