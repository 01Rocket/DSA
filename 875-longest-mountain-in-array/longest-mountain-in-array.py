class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        longest = 0
        i = 1

        while i < n - 1:
            # Check if current element is the peak
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:

                left = i
                right = i

                # Move left while increasing
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                # Move right while decreasing
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                longest = max(longest, right - left + 1)

                # Skip checked elements
                i = right
            else:
                i += 1

        return longest