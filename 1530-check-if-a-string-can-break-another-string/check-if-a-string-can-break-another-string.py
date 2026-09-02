class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)

        # Check if s1 can break s2
        can_s1_break = all(a >= b for a, b in zip(s1, s2))

        # Check if s2 can break s1
        can_s2_break = all(b >= a for a, b in zip(s1, s2))

        return can_s1_break or can_s2_break