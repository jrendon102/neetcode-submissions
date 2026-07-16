class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Base case: a single element is already sorted
        if len(nums) <= 1:
            return nums
            
        # 1. Divide: Find the midpoint and split the array
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        # 2. Conquer: Merge the two sorted halves
        return self._merge(left_half, right_half)
        
    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        res = []
        l = r = 0
        
        # Compare elements from both halves and merge them in order
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
                
        # Append any remaining elements (similar to Merge Strings Alternately!)
        res.extend(left[l:])
        res.extend(right[r:])
        return res