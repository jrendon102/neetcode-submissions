class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity automatically becomes O(nlog(n))
        nums.sort()

        # A + B = C ----> B + C = -A 
        # This becomes a 2Sum problem using 2 ptr (2Sum uses 2 pts but only if arr is sorted)
        # [-1,0,1,2,-1,-4] ----> [-4,-1,-1,0,1,2]
        res = []
        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n - 1]:
                continue
            target = -nums[n]
            l = n + 1
            r = len(nums) -  1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum == target:
                    res.append([nums[l], nums[r], nums[n]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return res

 


