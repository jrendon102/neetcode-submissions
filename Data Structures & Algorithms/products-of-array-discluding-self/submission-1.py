class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        # Step 1: Calculate prefix products (left to right)
        prefix_prod = 1
        for i in range(n):
            res[i] = prefix_prod
            prefix_prod *= nums[i]
            
        # Step 2: Calculate suffix products and multiply inline (right to left)
        suffix_prod = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix_prod
            suffix_prod *= nums[i]
            
        return res