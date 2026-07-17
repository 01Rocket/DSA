class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Find the initial sum of even numbers
        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num

        answer = []

        # Process each query
        for value, index in queries:
            # Remove the current value if it is even
            if nums[index] % 2 == 0:
                even_sum -= nums[index]

            # Update the array
            nums[index] += value

            # Add the updated value if it is even
            if nums[index] % 2 == 0:
                even_sum += nums[index]

            # Store the current even sum
            answer.append(even_sum)

        return answer