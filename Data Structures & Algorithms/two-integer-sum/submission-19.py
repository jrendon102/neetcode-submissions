class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stash = {}
        for n in range(len(nums)):
            diff = target - nums[n]
            if stash.get(diff) is not None:
                return [stash[diff], n]
            stash[nums[n]] = n
        return []