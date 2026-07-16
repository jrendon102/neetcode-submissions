class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums_map.get(diff) is not None:
                return [nums_map[diff], i]
            nums_map[nums[i]] = i 
