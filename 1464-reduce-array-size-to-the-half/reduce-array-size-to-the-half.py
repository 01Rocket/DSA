class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        frequencies = sorted(freq.values(), reverse=True)

        removed = 0
        answer = 0
        half = len(arr) // 2

        for count in frequencies:
            removed += count
            answer += 1

            if removed >= half:
                break

        return answer