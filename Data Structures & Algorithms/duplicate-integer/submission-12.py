class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stash = set()
        for n in nums:
            if n in stash:
                return True
            stash.add(n)
        return False