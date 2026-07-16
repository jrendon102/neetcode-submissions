class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None
        count = 0
        for n in nums:
            if count == 0:
                cand = n
                count = 1
            elif n == cand:
                count += 1
            elif n != cand:
                count -= 1
        return cand