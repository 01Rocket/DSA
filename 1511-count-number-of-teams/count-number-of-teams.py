class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0

        for j in range(n):
            left_small = 0
            left_large = 0
            right_small = 0
            right_large = 0

            # Check soldiers before j
            for i in range(j):
                if rating[i] < rating[j]:
                    left_small += 1
                else:
                    left_large += 1

            # Check soldiers after j
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_small += 1
                else:
                    right_large += 1

            # Increasing teams + decreasing teams
            teams += left_small * right_large
            teams += left_large * right_small

        return teams