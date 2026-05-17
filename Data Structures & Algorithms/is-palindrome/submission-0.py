class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string

        clean_text = s.translate(str.maketrans("", "", string.punctuation)).lower().replace(" ", "")

        reversed = ""
        for character in clean_text:
            reversed = character + reversed

        if clean_text == reversed:
            return True

        return False
