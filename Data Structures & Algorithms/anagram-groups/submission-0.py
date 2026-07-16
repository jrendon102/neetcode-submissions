class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            alphabet = [0] * 26
            for char in word:
                value = ord(char) - ord('a')
                alphabet[value] += 1
            signature = tuple(alphabet)
            if signature in anagram_map:
                anagram_map[signature].append(word)
            else:
                anagram_map[signature] = [word]
        return list(anagram_map.values())