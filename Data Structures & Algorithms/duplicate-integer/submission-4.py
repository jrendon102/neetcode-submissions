class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for num in range(len(nums)):
            if nums[num] in dup:
                return True
            dup.add(nums[num])
        return False
        