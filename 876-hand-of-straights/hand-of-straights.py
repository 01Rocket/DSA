class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Total cards must be divisible by group size
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        # Process cards in sorted order
        for card in sorted(count):
            while count[card] > 0:
                # Try to form one group
                for num in range(card, card + groupSize):
                    if count[num] == 0:
                        return False
                    count[num] -= 1

        return True