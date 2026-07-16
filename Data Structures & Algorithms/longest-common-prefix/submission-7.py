class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Vertical Scanning
        Treat as matrix and iterate column-by-column across rows
        strs = ["dance", "dag", "danger"]
        
        Think of this like a matrix but jagged:
        ---> strs = [
                        "dance",    Row 0
                        "dag",      Row 1
                        "danger"    Row 2
                    ]
        """
        res = ""
        for c in range(len(strs[0])):
            pre = strs[0][c]
            for r in range(len(strs)):
                if c >= len(strs[r]) or strs[r][c] != pre:
                    return res
            res += pre
        return res




