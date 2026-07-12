class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)

        group = 0

        for freq in count.values():
            group = gcd(group, freq)

        return group >= 2