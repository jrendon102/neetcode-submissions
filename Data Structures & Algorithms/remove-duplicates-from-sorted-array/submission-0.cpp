class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int p1 = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[i - 1]) {
                nums[p1 + 1] = nums[i];
                p1++;
            }
        }
        return p1 + 1;
    }
};