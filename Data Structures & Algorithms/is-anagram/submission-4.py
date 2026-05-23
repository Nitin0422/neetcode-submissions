class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_ascii = [0] * 26
        t_ascii = [0] * 26

        for i in range(len(s)):
            s_ascii[ord(s[i]) - ord("a")] += 1
            t_ascii[ord(t[i]) - ord("a")] += 1

        return s_ascii == t_ascii
