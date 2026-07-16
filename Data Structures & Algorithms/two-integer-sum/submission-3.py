class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stash = dict()
        for index, value in enumerate(nums):
            diff = target - value
            if stash.get(diff) is not None:
                return [stash.get(diff), index]
            stash[value] = index 
