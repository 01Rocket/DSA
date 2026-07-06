class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)

        # Step 1: put words in buckets based on first character
        for word in words:
            waiting[word[0]].append(word[1:])

        count = 0

        # Step 2: scan through s
        for ch in s:
            old_list = waiting[ch]
            waiting[ch] = []

            for rest in old_list:
                if len(rest) == 0:
                    count += 1
                else:
                    waiting[rest[0]].append(rest[1:])

        return count