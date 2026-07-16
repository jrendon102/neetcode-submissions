class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int leftPtr = 0;
        int rightPtr = nums.size() - 1;
        int temp;
        while (leftPtr <= rightPtr) {
            if (nums[leftPtr] == val) {
                temp = nums[leftPtr];
                nums[leftPtr] = nums[rightPtr];
                nums[rightPtr] = temp;
                rightPtr -= 1;
            }
            else {
                leftPtr += 1;
            }
        }
        return leftPtr;
    }
};