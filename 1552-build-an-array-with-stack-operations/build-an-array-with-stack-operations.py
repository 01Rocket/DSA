class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        target_index = 0

        for num in range(1, n + 1):
            result.append("Push")

            if num != target[target_index]:
                result.append("Pop")
            else:
                target_index += 1

            # Stop once we have built the target
            if target_index == len(target):
                break

        return result