class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []

        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                digits.append(ch)

        if abs(len(letters) - len(digits)) > 1:
            return ""

        result = []

        # Start with the group having more characters
        if len(letters) >= len(digits):
            first = letters
            second = digits
        else:
            first = digits
            second = letters

        for i in range(len(first)):
            result.append(first[i])

            if i < len(second):
                result.append(second[i])

        return "".join(result)