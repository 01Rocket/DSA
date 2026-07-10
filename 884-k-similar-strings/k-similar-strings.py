class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        queue = deque([(s1, 0)])
        visited = {s1}

        while queue:
            current, steps = queue.popleft()

            i = 0
            while current[i] == s2[i]:
                i += 1

            for j in range(i + 1, len(current)):
                if current[j] == s2[i] and current[j] != s2[j]:
                    chars = list(current)
                    chars[i], chars[j] = chars[j], chars[i]
                    new_string = "".join(chars)

                    if new_string == s2:
                        return steps + 1

                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append((new_string, steps + 1))

        return -1