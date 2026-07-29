class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # Store frequency of each unique word mask
        freq = {}

        for word in words:
            mask = 0
            for ch in set(word):          # Ignore duplicate letters
                mask |= 1 << (ord(ch) - ord('a'))

            # Words with more than 7 unique letters can never match
            if mask.bit_count() <= 7:
                freq[mask] = freq.get(mask, 0) + 1

        answer = []

        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))

            # Mask of the last six letters
            mask = 0
            for ch in puzzle[1:]:
                mask |= 1 << (ord(ch) - ord('a'))

            count = 0
            subset = mask

            while True:
                current = subset | first
                count += freq.get(current, 0)

                if subset == 0:
                    break

                subset = (subset - 1) & mask

            answer.append(count)

        return answer