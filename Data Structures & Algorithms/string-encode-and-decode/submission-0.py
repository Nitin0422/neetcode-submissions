class Solution:

    def encode(self, strs: List[str]) -> str:
        # This should convert list of strings into a single string
        sentence = ""
        
        for word in strs:
            sentence = sentence + str(len(word)) + "#" + word
        
        return sentence

    def decode(self, s: str) -> List[str]:
        # This should convert a single long string into a list of string
        res, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res