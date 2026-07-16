class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums, 0, nums.size() - 1);
        return nums;
    }
private:
    void mergeSort(vector<int>& nums, int leftIndex, int rightIndex) {
        if (leftIndex >= rightIndex) return;
        int midIndex = leftIndex + (rightIndex - leftIndex) / 2;

        // Divide
        mergeSort(nums, leftIndex, midIndex);
        mergeSort(nums, midIndex + 1, rightIndex);

        // Conquer
        merge(nums, leftIndex, midIndex, rightIndex);
    }
    void merge(vector<int>& nums, int leftIndex, int midIndex, int rightIndex) {
        // vector<int> leftArr(nums.begin() + leftIndex, nums.begin() + midIndex + 1);
        // vector<int> rightArr(nums.begin() + midIndex + 1, nums.begin() + rightIndex + 1);
        
        vector<int> leftArr(midIndex - leftIndex + 1);
        vector<int> rightArr(rightIndex - midIndex);

        for (int i = 0; i < leftArr.size(); i++) {
            leftArr[i] = nums[leftIndex + i];
        }
        for (int i = 0; i < rightArr.size(); i++) {
            rightArr[i] = nums[midIndex + 1 + i];
        }

        int leftPtr = 0, rightPtr = 0, index = leftIndex;
        while (leftPtr < leftArr.size() && rightPtr < rightArr.size()) {
            if (leftArr[leftPtr] <= rightArr[rightPtr]) {
                nums[index++] = leftArr[leftPtr++];
            }
            else {
                nums[index++] = rightArr[rightPtr++];
            }
        }

        while (leftPtr < leftArr.size()) {
            nums[index] = leftArr[leftPtr];
            leftPtr++;
            index++;
        }

        while (rightPtr < rightArr.size()) {
            nums[index] = rightArr[rightPtr];
            rightPtr++;
            index++;
        }

    }
};