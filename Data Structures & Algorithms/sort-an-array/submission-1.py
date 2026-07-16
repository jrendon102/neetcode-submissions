class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <=1:
            return nums

        mid = len(nums) // 2
        left_array = self.sortArray(nums[:mid])
        right_array = self.sortArray(nums[mid:])

        return self.merge(left_array, right_array)

    def merge(self, left_array, right_array):
        left_ptr = 0
        right_ptr = 0
        res = []

        while left_ptr < len(left_array) and right_ptr < len(right_array):
            if left_array[left_ptr] <= right_array[right_ptr]:
                res.append(left_array[left_ptr])
                left_ptr += 1
            else:
                res.append(right_array[right_ptr])
                right_ptr += 1
        
        res.extend(left_array[left_ptr:])
        res.extend(right_array[right_ptr:])
        
        return res