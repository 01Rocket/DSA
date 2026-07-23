class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        total = 0
        total_sum = 0
        minimum = -1
        maximum = 0
        mode = 0
        mode_count = 0

        for i in range(256):
            if count[i] > 0:
                if minimum == -1:
                    minimum = i
                maximum = i
                total += count[i]
                total_sum += i * count[i]

                if count[i] > mode_count:
                    mode_count = count[i]
                    mode = i

        mean = total_sum / total

        if total % 2 == 1:
            left = right = total // 2 + 1
        else:
            left = total // 2
            right = left + 1

        curr = 0
        first = second = 0

        for i in range(256):
            curr += count[i]

            if curr >= left and first == 0:
                first = i

            if curr >= right:
                second = i
                break

        median = (first + second) / 2.0

        return [float(minimum), float(maximum), mean, median, float(mode)]