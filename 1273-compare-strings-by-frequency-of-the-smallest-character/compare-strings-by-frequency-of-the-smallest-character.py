class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def frequency(s):
            smallest = min(s)
            return s.count(smallest)

        word_freq = []

        for word in words:
            word_freq.append(frequency(word))

        word_freq.sort()

        answer = []

        for query in queries:
            q = frequency(query)
            index = bisect_right(word_freq, q)
            answer.append(len(word_freq) - index)

        return answer