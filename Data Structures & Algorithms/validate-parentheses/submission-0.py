class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in close_open_map:
                if stack and stack[-1] == close_open_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
