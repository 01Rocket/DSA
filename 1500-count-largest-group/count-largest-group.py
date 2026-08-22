class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}

        # Calculate digit sum and count each group
        for num in range(1, n + 1):
            digit_sum = sum(map(int, str(num)))
            groups[digit_sum] = groups.get(digit_sum, 0) + 1

        # Find the largest group size
        largest = max(groups.values())

        # Count groups having that size
        return sum(1 for size in groups.values() if size == largest)