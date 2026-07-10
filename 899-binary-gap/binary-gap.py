class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]

        last = -1
        answer = 0

        for i in range(len(binary)):
            if binary[i] == '1':
                if last != -1:
                    answer = max(answer, i - last)
                last = i

        return answer