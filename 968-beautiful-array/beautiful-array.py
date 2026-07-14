class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        result = [1]

        while len(result) < n:
            next_array = []

            # Add odd numbers
            for num in result:
                if 2 * num - 1 <= n:
                    next_array.append(2 * num - 1)

            # Add even numbers
            for num in result:
                if 2 * num <= n:
                    next_array.append(2 * num)

            result = next_array

        return result