class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter

        char_count = Counter(chars)
        total = 0

        for word in words:
            word_count = Counter(word)
            valid = True

            for ch in word_count:
                if word_count[ch] > char_count.get(ch, 0):
                    valid = False
                    break

            if valid:
                total += len(word)

        return total