class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        if (nums.size() <= 1) return nums;
        vector<int>temp(nums.size());
        mergeSort(nums, temp, 0, nums.size() - 1);
        return nums;
    }
private:
    void mergeSort(vector<int>& nums, vector<int>& temp, int left, int right) {
        if (left >= right) return;
        int mid = left + (right - left) / 2;
        mergeSort(nums, temp, left, mid);
        mergeSort(nums, temp, mid + 1, right);
        int l = left, r = mid + 1, k = left;
        while (l <= mid && r <= right) {
            if (nums[l] <= nums[r]) {
                temp[k] = nums[l];
                l++;
                k++;
            }
            else {
                temp[k] = nums[r];
                r++;
                k++;
            }
        }
        
        while (l <= mid) {
            temp[k] = nums[l];
            l++;
            k++;
        }

        while(r <= right) {
            temp[k] = nums[r];
            r++;
            k++;
        }

        for (int i = left; i <= right; i++) {
            nums[i] = temp[i];
        }
    }
};