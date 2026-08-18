class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        first = {0: -1}
        mask = 0
        answer = 0

        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}

        for i, ch in enumerate(s):
            if ch in vowels:
                mask ^= vowels[ch]

            if mask in first:
                answer = max(answer, i - first[mask])
            else:
                first[mask] = i

        return answer