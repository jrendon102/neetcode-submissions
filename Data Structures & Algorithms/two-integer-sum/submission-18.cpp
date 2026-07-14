class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> stash;
        vector<int> res(2);
        int diff;
        for (int i = 0; i < nums.size(); i++) {
            diff = target - nums[i];
            if (stash.contains(diff)) {
                res[0] = stash[diff];
                res[1] = i;
                return res;
            }
            stash[nums[i]] = i;
        }
        return res;
    }
};
