class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = {}

        # Count required letters from licensePlate
        for ch in licensePlate.lower():
            if ch.isalpha():
                need[ch] = need.get(ch, 0) + 1

        answer = ""

        for word in words:
            count = {}

            # Count letters in the current word
            for ch in word:
                count[ch] = count.get(ch, 0) + 1

            valid = True
            for ch in need:
                if count.get(ch, 0) < need[ch]:
                    valid = False
                    break

            if valid:
                if answer == "" or len(word) < len(answer):
                    answer = word

        return answer