class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_set:
                return [num_set[diff], i]
            num_set[n] = i