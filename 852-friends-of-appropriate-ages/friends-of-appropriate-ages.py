class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        n = len(ages)

        answer = 0
        left = 0
        right = 0

        for i in range(n):
            age = ages[i]

            if age < 15:
                continue

            while ages[left] <= 0.5 * age + 7:
                left += 1

            while right + 1 < n and ages[right + 1] <= age:
                right += 1

            answer += right - left

        return answer