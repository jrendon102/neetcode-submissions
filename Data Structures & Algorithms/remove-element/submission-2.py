class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left_ptr = 0
        right_ptr = len(nums) - 1

        while left_ptr <= right_ptr:
            if nums[left_ptr] == val:
                temp = nums[left_ptr]
                nums[left_ptr] = nums[right_ptr]
                nums[right_ptr] = temp
                right_ptr -= 1
            else:
                left_ptr += 1
        return left_ptr