class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = {}
        freq = {}
        ans = 0
        max_freq = 0

        for i, num in enumerate(nums):
            if num in count:
                f = count[num]
                freq[f] -= 1
                if freq[f] == 0:
                    del freq[f]

            count[num] = count.get(num, 0) + 1
            f = count[num]
            freq[f] = freq.get(f, 0) + 1
            max_freq = max(max_freq, f)

            if max_freq == 1:
                ans = i + 1
            elif freq.get(max_freq, 0) * max_freq + 1 == i + 1:
                ans = i + 1
            elif freq.get(1, 0) == 1 and freq.get(max_freq, 0) * max_freq + 1 == i + 1:
                ans = i + 1
            elif freq.get(max_freq, 0) == 1 and (max_freq - 1) * (freq.get(max_freq - 1, 0) + 1) == i:
                ans = i + 1

        return ans