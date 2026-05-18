class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        print(len(s))
        for i in range(len(s)):
            seen_chars = s[i]
            length = 1
            for j in range(i + 1, len(s)):
                if s[j] not in seen_chars:
                    seen_chars += s[j]
                    length += 1
                else:
                    break

            
            max_length = max(length, max_length)

        return max_length        