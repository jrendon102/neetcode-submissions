class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_map = {}
        for n in nums:
            if n in num_map:
                num_map[n] += 1
            else:
                num_map[n] = 1
        res = []
        target = len(nums) // 3
        for key, val in num_map.items():
            if val > target:
                res.append(key)
            
        return res