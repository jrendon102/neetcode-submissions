class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stash = {}
        for n in nums:
            if n in stash:
                stash[n] += 1
            else:
                stash[n] = 1
        for key, val in stash.items():
            if val >= len(nums) // 2:
                return key
        