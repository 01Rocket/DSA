class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def matches(word):
            i = 0

            for ch in word:
                if i < len(pattern) and ch == pattern[i]:
                    i += 1
                elif ch.isupper():
                    return False

            return i == len(pattern)

        answer = []

        for word in queries:
            answer.append(matches(word))

        return answer