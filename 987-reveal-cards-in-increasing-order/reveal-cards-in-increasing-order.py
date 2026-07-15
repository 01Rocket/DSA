class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)

        result = [0] * n
        positions = deque(range(n))

        for card in deck:
            index = positions.popleft()
            result[index] = card

            if positions:
                positions.append(positions.popleft())

        return result