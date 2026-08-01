class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        # Count frequency of each number
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        seen = set()

        # Check if any frequency is repeated
        for freq in count.values():
            if freq in seen:
                return False
            seen.add(freq)

        return True