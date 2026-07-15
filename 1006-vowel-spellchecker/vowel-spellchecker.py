class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def mask(word):
            result = ""
            for ch in word.lower():
                if ch in "aeiou":
                    result += "*"
                else:
                    result += ch
            return result

        exact = set(wordlist)
        case_map = {}
        vowel_map = {}

        for word in wordlist:
            lower = word.lower()

            if lower not in case_map:
                case_map[lower] = word

            key = mask(word)
            if key not in vowel_map:
                vowel_map[key] = word

        answer = []

        for query in queries:
            if query in exact:
                answer.append(query)
            elif query.lower() in case_map:
                answer.append(case_map[query.lower()])
            elif mask(query) in vowel_map:
                answer.append(vowel_map[mask(query)])
            else:
                answer.append("")

        return answer