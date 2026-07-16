class Solution:
    def isValid(self, s: str) -> bool:
        pattern = {
            "}":"{",
            "]":"[",
            ")":"(",
        }

        stack = []
        for c in s:
            if c in pattern and len(stack) > 0:
                val = pattern.get(c)
                stack_val = stack.pop()
                if val != stack_val:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        