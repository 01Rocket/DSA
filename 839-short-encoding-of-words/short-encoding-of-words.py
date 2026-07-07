class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # Remove duplicate words
        word_set = set(words)

        # Remove all suffixes
        for word in words:
            for i in range(1, len(word)):
                word_set.discard(word[i:])

        # Calculate total length
        answer = 0
        for word in word_set:
            answer += len(word) + 1

        return answer