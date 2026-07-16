class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            while prefix not in s:
                prefix = prefix[:-1]
                if not prefix:
                    return prefix
        return prefix