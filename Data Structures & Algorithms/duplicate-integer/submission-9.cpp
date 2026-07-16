class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> stash;
        for (int i = 0; i < nums.size(); i++) {
            if (stash.count(nums[i])) {
                return true;
            }
            stash.insert(nums[i]);
        }
        return false;
    }
};