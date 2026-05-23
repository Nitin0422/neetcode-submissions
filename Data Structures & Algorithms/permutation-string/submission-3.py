class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Initialize two dictionaries for setting up ascii checks
        s1_ascii = {i: 0 for i in range(26)}
        s2_ascii = {i: 0 for i in range(26)}

        # Map ascii for the first string also check first window for s2
        for i in range(len(s1)):
            s1_ascii[ord(s1[i]) - ord("a")] += 1
            s2_ascii[ord(s2[i]) - ord("a")] += 1

        matches = 0

        # Check matches in the first window
        for i in range(26):
            if s1_ascii[i] == s2_ascii[i]:
                matches += 1

        # Slide the window and check
        left = 0
        for right in range(len(s1), len(s2)):
            # Return if permutation found
            if matches == 26:
                return True

            # ASCII value of the new character added to right
            ascii_val = ord(s2[right]) - ord("a")
            s2_ascii[ascii_val] += 1

            # if newly added character is in the lookup string
            if s1_ascii[ascii_val] == s2_ascii[ascii_val]:
                matches += 1
            # if we increased the character in the lookup string
            elif s1_ascii[ascii_val] + 1 == s2_ascii[ascii_val]:
                matches -= 1

            # ASCII value of the old character removed from left
            ascii_val = ord(s2[left]) - ord("a")
            s2_ascii[ascii_val] -= 1

            # if removed character was a match.
            if s1_ascii[ascii_val] == s2_ascii[ascii_val]:
                matches += 1
            # if we increased the character in the lookup string
            elif s1_ascii[ascii_val] - 1 == s2_ascii[ascii_val]:
                matches -= 1

            left += 1

        return matches == 26
