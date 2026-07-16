class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> stash;
        vector<int> res;
        for (int i=0; i< nums.size(); i++) {
            int diff = target - nums[i];
            if (stash.contains(diff)) {
                res.push_back(stash[diff]);
                res.push_back(i);
                return res;
            }
            stash[nums[i]] = i;
        }
        return res;
    }
};
