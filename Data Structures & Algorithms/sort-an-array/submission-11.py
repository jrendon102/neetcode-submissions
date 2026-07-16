class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums: List[int], leftIndex: int, rightIndex: int):
        if leftIndex >= rightIndex: return

        # Divide
        # midIndex = len(nums) // 2
        midIndex = (leftIndex + rightIndex) // 2
        self.mergeSort(nums, leftIndex, midIndex)
        self.mergeSort(nums,midIndex + 1, rightIndex)
        
        # Conquer
        self.merge(nums, leftIndex, midIndex, rightIndex)
        
    def merge(self, nums: List[int], leftIndex: int, midIndex: int, rightIndex: int):
        leftArr = [None] * ((midIndex - leftIndex) + 1)
        rightArr = [None] * (rightIndex - midIndex)
        for i in range(len(leftArr)):
            leftArr[i] = nums[leftIndex + i]
        for i in range(len(rightArr)):
            rightArr[i] = nums[midIndex + i + 1]

        leftPtr = 0
        rightPtr = 0
        k = leftIndex

        while leftPtr < len(leftArr) and rightPtr < len(rightArr):
            if leftArr[leftPtr] <= rightArr[rightPtr]:
                nums[k] = leftArr[leftPtr]
                k+=1
                leftPtr += 1
            else:
                nums[k] = rightArr[rightPtr]
                k+=1
                rightPtr += 1

        while leftPtr < len(leftArr):
                nums[k] = leftArr[leftPtr]
                k+=1
                leftPtr += 1

        while rightPtr < len(rightArr):
                nums[k] = rightArr[rightPtr]
                k+=1
                rightPtr += 1

