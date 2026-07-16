class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stash = dict()
        for index, value in enumerate(nums):
            diff = target - value
            if diff in stash:
                return [stash[diff], index]
            stash[value] = index 
