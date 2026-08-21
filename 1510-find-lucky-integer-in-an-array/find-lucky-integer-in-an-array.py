class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}

        # Count frequency of each number
        for num in arr:
            count[num] = count.get(num, 0) + 1

        lucky = -1

        # Check which numbers are lucky
        for num in count:
            if count[num] == num:
                lucky = max(lucky, num)

        return lucky