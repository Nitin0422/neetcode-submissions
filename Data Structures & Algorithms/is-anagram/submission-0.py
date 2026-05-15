class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_babu = sorted(list(s))
        t_babu = sorted(list(t))

        print(s_babu, t_babu)
        if s_babu == t_babu:
            return True
        else:
            return False