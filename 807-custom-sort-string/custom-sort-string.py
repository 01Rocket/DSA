class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}

        # Count frequency of each character
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        result = ""

        # Add characters according to the given order
        for ch in order:
            if ch in count:
                result += ch * count[ch]
                del count[ch]

        # Add remaining characters
        for ch in count:
            result += ch * count[ch]

        return result