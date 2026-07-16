class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> stash;
        vector<int> res(2);
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (stash.count(diff) == 1) {
                res[0] = stash[diff];
                res[1] = i;
                return res;
            }
                stash[nums[i]] = i;
        }
        return res;
    }
};
