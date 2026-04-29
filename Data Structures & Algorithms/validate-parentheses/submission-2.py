class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mappings = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in mappings:
                if not stack or stack[-1] != mappings[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return len(stack) == 0
        