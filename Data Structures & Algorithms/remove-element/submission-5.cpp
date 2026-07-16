class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int l = 0;
        int r = nums.size() - 1;
        while (l <= r) {
            if (nums[l] == val) {
                int temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;
                r -= 1;
            }
            else {
                l += 1;
            }
        }   
        return l;
    }
};