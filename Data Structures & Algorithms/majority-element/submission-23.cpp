class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> stash;
        for (int i = 0; i < nums.size(); i++) {
            if (stash.count(nums[i]) == 0) {
                stash[nums[i]] = 1;
            }
            else {
                stash[nums[i]] += 1;
            }
        }
        int res;
        for (auto it = stash.begin(); it != stash.end(); it++) {
            if (it->second >= nums.size()/2) {
                res = it->first;
            }
        }
        return res;
    }
};