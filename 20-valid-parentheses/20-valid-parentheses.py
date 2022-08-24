class Solution:
    def isValid(self, s: str) -> bool:
        chars = {')': '(', '}': '{', ']':'['}
        stack = []
        for c in s:
            if c in chars:
                if not stack or stack[-1] != chars[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack