class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        pre = [prod]
        for n in range(1, len(nums)):
            prod *= (nums[n-1])
            pre.append(prod)
        
        prod = 1
        suff = [prod]
        for n in range(len(nums)-1, 0, -1):
            prod *= nums[n]
            suff.append(prod)

        n = len(suff) - 1
        res = []
        print(pre)
        print(suff)
        for i in pre:
            res.append(i* suff[n])
            n -=  1
        return res




            
            
            