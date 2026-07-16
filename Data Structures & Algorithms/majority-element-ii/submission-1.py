class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_1 = None
        candidate_2 = None
        count_1 = 0
        count_2 = 0

        # Shows which nums are majority
        for n in nums:
            if n == candidate_1:
                count_1 += 1
            elif n == candidate_2:
                count_2 += 1
            elif count_1 == 0:
                candidate_1 = n
                count_1 = 1
            elif count_2 == 0:
                candidate_2 =n
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1

        # Verifies which one(s) are > n/3
        res = []
        threshold = len(nums) // 3
        count_1 = 0
        count_2 = 0
        for n in nums:
            if n == candidate_1:
                count_1 += 1
            elif n == candidate_2:
                count_2 += 1
            else:
                pass
        if count_1 > threshold:
            res.append(candidate_1)
        if count_2 > threshold:
            res.append(candidate_2)
        return res