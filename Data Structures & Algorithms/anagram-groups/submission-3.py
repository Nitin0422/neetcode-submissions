class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for word in strs:
            ascii_val = [0] * 26

            for letter in word:
                ascii_val[ord(letter) - ord("a")] += 1

            res[tuple(ascii_val)].append(word)

        return list(res.values())
