class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)

        # Sort by frequency (highest first)
        nums = sorted(count.items(), key=lambda x: -x[1])

        result = [0] * len(barcodes)
        index = 0

        for num, freq in nums:
            while freq > 0:
                result[index] = num
                index += 2

                if index >= len(barcodes):
                    index = 1

                freq -= 1

        return result