class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = Counter()
        frequency = Counter()
        left = 0
        answer = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # Keep the window size equal to minSize
            if right - left + 1 > minSize:
                count[s[left]] -= 1

                if count[s[left]] == 0:
                    del count[s[left]]

                left += 1

            # Check the current substring
            if right - left + 1 == minSize and len(count) <= maxLetters:
                substring = s[left:right + 1]
                frequency[substring] += 1
                answer = max(answer, frequency[substring])

        return answer