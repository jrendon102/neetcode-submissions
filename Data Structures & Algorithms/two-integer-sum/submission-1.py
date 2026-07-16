class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {}
        for n in range(len(nums)):
            diff = target - nums[n]
            if nMap.get(diff) is not None:
                return [nMap.get(diff), n]
            nMap[nums[n]] = n 
        