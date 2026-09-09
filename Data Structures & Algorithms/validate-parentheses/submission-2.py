class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False
        stack = []
        brackets = "({["
        map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack or map[char] != stack.pop():
                    return False

        return len(stack) == 0

        
        