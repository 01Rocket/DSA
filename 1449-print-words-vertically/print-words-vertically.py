class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        result = []

        # Find the longest word
        max_len = max(len(word) for word in words)

        # Build each row vertically
        for i in range(max_len):
            row = ""

            for word in words:
                if i < len(word):
                    row += word[i]
                else:
                    row += " "

            # Remove trailing spaces
            result.append(row.rstrip())

        return result