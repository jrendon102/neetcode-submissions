class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_map = {}
        for n in nums:
            if n in num_map:
                num_map[n] += 1
            else:
                num_map[n] = 1
        
        freq = 0
        res = nums[0]
        for key, val in num_map.items():
            if val > freq:
                freq = val
                res = key
        return res
        
                

