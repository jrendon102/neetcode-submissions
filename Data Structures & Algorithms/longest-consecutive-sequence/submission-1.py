class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0
        for n in num_set:
            i = n + 1
            current_max_seq = 1
            if n-1 not in num_set:
                while i in num_set:
                    i += 1
                    current_max_seq += 1
            max_seq = max(max_seq, current_max_seq)
        return max_seq

            
        