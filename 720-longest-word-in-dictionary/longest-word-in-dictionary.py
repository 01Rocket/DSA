class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()  # ensures lexicographic order for same length
        words.sort(key=len)

        valid = set([""])
        answer = ""

        for word in words:
            if word[:-1] in valid:
                valid.add(word)

                if len(word) > len(answer):
                    answer = word
                elif len(word) == len(answer) and word < answer:
                    answer = word

        return answer