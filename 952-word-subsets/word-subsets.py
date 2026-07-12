class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required = [0] * 26

        # Find the maximum frequency needed for each letter
        for word in words2:
            count = Counter(word)
            for ch, freq in count.items():
                index = ord(ch) - ord('a')
                required[index] = max(required[index], freq)

        answer = []

        # Check each word in words1
        for word in words1:
            count = Counter(word)
            valid = True

            for i in range(26):
                if count.get(chr(i + ord('a')), 0) < required[i]:
                    valid = False
                    break

            if valid:
                answer.append(word)

        return answer