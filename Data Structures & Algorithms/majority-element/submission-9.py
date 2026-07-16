class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_map = {}
        for n in nums:
            if n in num_map:
                num_map[n] += 1
            else:
                num_map[n] = 1

        res = 0
        freq = 1
        print(num_map)
        for key, val in num_map.items():
            if val >= freq:
                print(f"{key}:{val}")
                res = key
                print(res)
            freq = max(val, freq)
        return res