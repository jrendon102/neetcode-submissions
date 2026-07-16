class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if num_map.get(diff) is not None:
                return [num_map[diff], i + 1]
            num_map[numbers[i]] = i + 1