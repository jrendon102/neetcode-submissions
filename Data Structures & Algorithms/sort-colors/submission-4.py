class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * 3
        for n in nums:
            if n == 0:
                bucket[0] += 1
            elif n == 1:
                bucket[1] += 1
            else:
                bucket[2] += 1
        index = 0
        for n in range(len(bucket)):
            for _ in range(bucket[n]):
                nums[index] = n
                index += 1
