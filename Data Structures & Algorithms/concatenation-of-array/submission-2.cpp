class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans(nums.size() * 2);
        int midIndex = nums.size();

        for (int i = 0; i < midIndex; i++) {
            ans[i] = nums[i];
            ans[i + midIndex] = nums[i];
        }
        return ans;
    }
};