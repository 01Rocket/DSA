class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)

        # Maximum sum ending at current position without deletion
        no_delete = arr[0]

        # Maximum sum ending at current position with one deletion
        one_delete = float("-inf")

        answer = arr[0]

        for i in range(1, n):
            one_delete = max(one_delete + arr[i], no_delete)
            no_delete = max(no_delete + arr[i], arr[i])

            answer = max(answer, no_delete, one_delete)

        return answer