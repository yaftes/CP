class Solution:
    def isValid(self, s: str) -> bool:
        char = {")":"(","}":"{","]":"["}
        stack = []
        for i in s:
            if i in char:
                if stack and stack[-1] == char[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False