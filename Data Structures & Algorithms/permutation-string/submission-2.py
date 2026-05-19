class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        window = len(s1)

        for r in range(len(s2)):
            if sorted((s2[l : window + l])) == sorted(s1):
                return True

            l += 1
        return False
