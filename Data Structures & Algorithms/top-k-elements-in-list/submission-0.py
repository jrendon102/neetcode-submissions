class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in nums:
            if n in freq_map:
                freq_map[n] += 1
            else:
                freq_map[n] = 1

        freq_bucket = [ [] for _ in range(len(nums) + 1)]
        
        for key, value in freq_map.items():
            freq_bucket[value].append(key)

        result = []
        for item in reversed(freq_bucket):
            if item and len(result) < k:
                result.extend(item)
        return result

        

