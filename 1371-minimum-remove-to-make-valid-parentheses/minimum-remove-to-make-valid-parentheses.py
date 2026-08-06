class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = []

        # Mark invalid closing brackets
        for i in range(len(chars)):
            if chars[i] == '(':
                stack.append(i)
            elif chars[i] == ')':
                if stack:
                    stack.pop()
                else:
                    chars[i] = ''

        # Remove unmatched opening brackets
        while stack:
            chars[stack.pop()] = ''

        return "".join(chars)