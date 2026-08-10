class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]

        for num in arr:
            prefix.append(prefix[-1] ^ num)

        answer = []

        for left, right in queries:
            answer.append(prefix[right + 1] ^ prefix[left])

        return answer