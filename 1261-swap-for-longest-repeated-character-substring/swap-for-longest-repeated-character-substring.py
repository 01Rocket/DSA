class Solution:
    def maxRepOpt1(self, text: str) -> int:
        from collections import Counter

        count = Counter(text)
        groups = []

        i = 0
        while i < len(text):
            j = i
            while j < len(text) and text[j] == text[i]:
                j += 1
            groups.append((text[i], j - i))
            i = j

        ans = 0

        # Check each group
        for ch, length in groups:
            if count[ch] > length:
                ans = max(ans, length + 1)
            else:
                ans = max(ans, length)

        # Merge two groups separated by one different character
        for i in range(1, len(groups) - 1):
            if groups[i][1] == 1 and groups[i - 1][0] == groups[i + 1][0]:
                ch = groups[i - 1][0]
                total = groups[i - 1][1] + groups[i + 1][1]
                if count[ch] > total:
                    total += 1
                ans = max(ans, total)

        return ans