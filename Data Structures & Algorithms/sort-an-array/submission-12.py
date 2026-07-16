class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Single upfront allocation
        temp = [0] * len(nums)
        self.mergeSort(nums, temp, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums: list[int], temp: list[int], left: int, right: int):
        if left >= right: 
            return

        mid = left + (right - left) // 2
        self.mergeSort(nums, temp, left, mid)
        self.mergeSort(nums, temp, mid + 1, right)
        
        self.merge(nums, temp, left, mid, right)
        
    def merge(self, nums: list[int], temp: list[int], left: int, mid: int, right: int):
        # Copy current state to temp
        for i in range(left, right + 1):
            temp[i] = nums[i]

        l = left
        r = mid + 1
        k = left

        # Read from temp, write to nums
        while l <= mid and r <= right:
            if temp[l] <= temp[r]:
                nums[k] = temp[l]
                l += 1
            else:
                nums[k] = temp[r]
                r += 1
            k += 1

        # Copy remaining left half elements
        while l <= mid:
            nums[k] = temp[l]
            l += 1
            k += 1