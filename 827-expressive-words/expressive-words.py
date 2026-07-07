class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def isStretchy(word):
            i = j = 0

            while i < len(s) and j < len(word):
                # Characters must match
                if s[i] != word[j]:
                    return False

                # Count same characters in s
                countS = 0
                ch = s[i]
                while i < len(s) and s[i] == ch:
                    countS += 1
                    i += 1

                # Count same characters in word
                countW = 0
                while j < len(word) and word[j] == ch:
                    countW += 1
                    j += 1

                # Invalid cases
                if countS < countW:
                    return False

                if countS != countW and countS < 3:
                    return False

            return i == len(s) and j == len(word)

        answer = 0

        for word in words:
            if isStretchy(word):
                answer += 1

        return answer