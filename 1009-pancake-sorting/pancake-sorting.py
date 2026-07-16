class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []

        def flip(k):
            arr[:k] = arr[:k][::-1]

        n = len(arr)

        for size in range(n, 1, -1):
            max_index = arr.index(size)

            if max_index == size - 1:
                continue

            if max_index != 0:
                flip(max_index + 1)
                answer.append(max_index + 1)

            flip(size)
            answer.append(size)

        return answer