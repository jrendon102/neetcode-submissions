class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> dup;
        for (int i = 0; i < nums.size(); i++) {
            if (dup.count(nums[i]) == 1) {
                return true;
            }
            else {
                dup.insert(nums[i]);
            }
        }
        return false;
    }
};