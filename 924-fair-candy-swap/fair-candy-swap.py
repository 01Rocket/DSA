class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)

        diff = (alice_total - bob_total) // 2

        bob_set = set(bobSizes)

        for candy in aliceSizes:
            need = candy - diff
            if need in bob_set:
                return [candy, need]