class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.answer = 0

        def backtrack(index, current):
            # Update maximum length
            self.answer = max(self.answer, len(current))

            # Try adding each remaining string
            for i in range(index, len(arr)):
                new_string = current + arr[i]

                # Check if all characters are unique
                if len(new_string) == len(set(new_string)):
                    backtrack(i + 1, new_string)

        backtrack(0, "")
        return self.answer