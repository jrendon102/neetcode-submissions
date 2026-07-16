class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        delimeter = "#"
        for word in strs:
            encoded_string += f"{len(word)}{delimeter}{word}"
        return encoded_string

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i : i + length])
            i += length
        return res
