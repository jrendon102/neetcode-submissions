class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> nMap;

        for(int n = 0; n < nums.size(); n++)
        {
            int diff = target - nums[n];
            if(nMap.find(diff) != nMap.end())
            {
                return {nMap[diff], n};
            }
            nMap[nums[n]] = n;
        }
    }
};
